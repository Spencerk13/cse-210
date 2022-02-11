class TerminalService:
     
    def read_guess(self, prompt):
        return (input(prompt))
        
    def write_text(self, text, newline=True):
        if newline:
            print(text)
        else:
            print(text, end="")
