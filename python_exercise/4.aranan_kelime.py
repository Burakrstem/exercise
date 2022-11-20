def find_word(metin):
    metin=metin.lower()
    metin=metin.replace(".","").replace(",","").replace("\n"," ")
    kelime=input("\naranacak kelime:")
    kelime=kelime.lower()
    metin=metin.split(" ")
    tekrar=metin.count(kelime)

    if tekrar>=1:
        for i in range(len(metin)):
           if metin[i]==kelime:
                print(f"{i+1}.kelime ={kelime}")
    else:
        print("kelime bulunamadi")

if __name__=='__main__':
    metin="""This document provides a preliminary overview of the VRX Competition 2022. The details of
    the competition are in draft status and subject to change. Tasks listed below may be added, modified or
    removed in response to community feedback or to better align with the overarching challenge
    objectives. A final version of the VRX Competition Documentation will be released in September 2021."""

    print(metin,"\n")
    find_word(metin)
