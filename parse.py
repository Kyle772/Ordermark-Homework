from bs4 import BeautifulSoup
import json


class HTMLParser():
    def __init__(self):
        self.json = None
        self.soup = None

    def run(self, htmlFile="", contentType="json"):
        self.soup = self.get_soup(htmlFile)
        if (contentType == "json"):
            parsed = self.parse(soup=self.soup)
            self.json = self.write_json(parsed=parsed)
            return self.json
        if (contentType == "soup"):
            return self.soup

    def get_soup(self, htmlFile=""):
        with open(htmlFile) as f:
            self.soup = BeautifulSoup(f, 'html.parser')
            return self.soup

    def parse(self, soup=None):
        jd = {}
        soup = self.soup

        jd["customer"] = {}
        jd["customer"]["name"] = soup.select_one('table > tr:nth-of-type(2) > td').string.strip()
        jd["customer"]["phone"] = soup.select_one('div[data-field="phone"]').string.strip()
        jd["customer_order_id"] = soup.select_one("div[id=cust_service_info]").string.strip().replace("Order ","")
        jd["menu_items"] = []
        for each in soup.select('div[data-section="menu-item"]'):
            temp = {}
            temp["id"] = int(each.select_one('div[menu-item-id]').get('menu-item-id'))
            temp["item_name"] = each.select_one('div[data-field="menu-item-name"]').string.strip()
            # Possible oversight of curency being dropped off
            temp["price"] = float(each.select_one('div[data-field="price"]').string.strip().replace("$",""))
            temp["quantity"] = int(each.select_one('div[data-field="quantity"]').string.strip())
            jd["menu_items"].append(temp)
        jd["restaurant"] = {}    
        jd["restaurant"]["restaurant_name"] = soup.select_one('div[data-field="restaurant-name"]').string.strip()
        
        return jd

    def write_json(self, parsed=None, jsonOut="parsed.json"):
        with open(jsonOut, 'w+') as of:
            json.dump(parsed, of, indent=4)
        return str(json.dumps(parsed))

if __name__ == "__main__":
    parse = HTMLParser()
    parsed = parse.run(htmlFile="parsing_input.html")
    print("Successfuly wrote JSON to file:\n%s".format(parsed))