class PDA:
    def __init__(self):
        self.stack = []
        self.current_state = 'q0'
    
    def transition(self, char):
        if self.current_state == 'q0':  # Başlangıç durumu
            if char == '(':
                self.stack.append(char)
                self.current_state = 'q1'
            elif char.isdigit():
                self.current_state = 'q2'
            else:
                self.current_state = 'rejected'
        
        elif self.current_state == 'q1':  # Parantez açıldıktan sonra
            if char == '(':
                self.stack.append(char)
            elif char.isdigit():
                self.current_state = 'q2'
            else:
                self.current_state = 'rejected'
        
        elif self.current_state == 'q2':  # Rakam gördükten sonra
            if char in '+-*/':
                self.current_state = 'q3'
            elif char == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    self.current_state = 'q4'
                else:
                    self.current_state = 'rejected'
            elif char.isdigit():
                self.current_state = 'q2'
            else:
                self.current_state = 'rejected'
        
        elif self.current_state == 'q3':  # Operatör gördükten sonra
            if char == '(':
                self.stack.append(char)
                self.current_state = 'q1'
            elif char.isdigit():
                self.current_state = 'q2'
            else:
                self.current_state = 'rejected'
        
        elif self.current_state == 'q4':  # Parantez kapandıktan sonra
            if char in '+-*/':
                self.current_state = 'q3'
            elif char == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                else:
                    self.current_state = 'rejected'
            else:
                self.current_state = 'rejected'
    
    def is_accepted(self, expression):
        self.stack = []
        self.current_state = 'q0'
        
        for char in expression:
            self.transition(char)
            if self.current_state == 'rejected':
                return False
        
        return self.current_state in {'q2', 'q4'} and not self.stack

# Kullanıcıdan girdi alma ve kontrol etme
def main():
    pda = PDA()
    while True:
        expression = input("Kontrol etmek istediğiniz matematiksel ifadeyi girin (çikmak için 'z' girin): ")
        if expression.lower() == 'z':
            break
        if pda.is_accepted(expression):
            print(f"İşlem: {expression}, İşlem geçerli")
        else:
            print(f"İşlem: {expression}, İşlem geçersiz")

if __name__ == "__main__":
    main()
