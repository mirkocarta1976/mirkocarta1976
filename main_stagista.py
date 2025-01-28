from stagista import Stagista

def main():
    stagisti=[]
    while True:
        numero_presenza = input("Inserisci il numero di ore di presenza:")
        if numero_presenza == "":
            break
        numero_identificativo = input("Inserisci il numero identificativo:")
        if numero_identificativo == "":
            break

        Stagisti = Stagista(numero_presenza,numero_identificativo)

        stagisti.append(Stagisti)
        Stagisti.set_stagista_numero(numero_presenza)
        Stagisti.set_stagista_identificativo(numero_identificativo)
        stagisti.append(Stagisti)

        stagisti_piu_giovane = max(stagisti, key=lambda x: x.get_stagista_identificativo())
        print(f"lo stagista piu giovane è colui con immatricolazione più alta ed è:{stagisti_piu_giovane._numero_identificativo}")

if __name__ == "__main__":
    main()
