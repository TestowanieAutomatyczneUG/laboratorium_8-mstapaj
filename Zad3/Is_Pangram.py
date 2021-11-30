
class Is_Pangram:
    def check(self, text):
        if isinstance(text, str):
            tab = []
            for i in text:
                if i not in tab and i != " " and i in 'abcdefghijklmnopqrstuvwxyz':
                    tab.append(i)
            if len(tab) > 25:
                return True
            else:
                return False
        else:
            raise Exception("Podane dane nie są stringiem")

