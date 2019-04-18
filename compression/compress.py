class Compressifyer():
    def __init__(self):
        self.st = ""
        self.position = 0
        self.ccount = 1
        self.output = ""

    def compress(self, s=""):
        self.st = s.lower()
        for letter in self.st:
            try: 
                # Check for end of string
                self.st[self.position+1] 
            except: 
                # If end of string append and break
                self.output += str(self.ccount) + letter
                self.position += 1
                self.ccount = 1
                break

            if letter == self.st[self.position+1]:
                # If current and next match
                self.ccount += 1
            else:
                # If they don't match append last batch
                if self.ccount <= 1:
                    # Don't show count if it's 1
                    self.output += letter
                else:
                    # Show count then letter
                    self.output += str(self.ccount) + letter
                self.ccount = 1
            # Next position
            self.position += 1

        return self.output

if __name__ == "__main__":
    c = Compressifyer()
    s = "aaabkKdee"
    print(c.compress(s=s))
