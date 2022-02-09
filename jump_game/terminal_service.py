class TerminalService:
     
    def _read_text(self, prompt):
        return input(prompt)

    def _read_guess(self, prompt):
        return (input(prompt))
        
    def _write_text(self, text):
        print(text)
