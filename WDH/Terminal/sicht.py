

def sicht(gein, gaus):
        saldo = sum(gein) - sum(gaus)
        print(f"""               Ihre Gesamteinnahmen betragen: {sum(gein)} €
               Ihre Gesamtausgaben betragen: {sum(gaus)} €
               Ihr Saldo beträgt: {saldo} €""")