#          TESTE - CÓDIGO GPT
class IndirectRules:
    def applyRule(self):
        indirect_rules = {
            '': '',
            '': '',           
        
        }
        return indirect_rules

class DirectRules:
    def applyRule(self):
        direct_rules = {
            '': '',
            '': ''

        }
        return direct_rules

class ChoiceRules:
    def __init__(self):
        self.regras = {
            'Indirect': IndirectRules(),
            'Direct': DirectRules()
        }

    def applyRule(self, type):
        regra = self.regras.get(type)
        if regra:
            return regra.applyRule()
        else:
            raise ValueError("Tipo de regra desconhecido")