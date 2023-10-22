#  Var GladSpexarnas Spärm 🍍

Spärmen i den *digitala* eran!

Var GladSpexarna hade under lång tid alla låtar från alla spex utskrivna på papper och satt i pärmar. Dessa delades ut under middagar, sittningar, etc. för att uppmuntra till sång och hygge.

Efter ca 20+ år av denna tradition började de flesta Spärmar falla sönder. Fler och fler låtar saknades och spärmarna uppdaterades mer och mer sällan. Ett godhjärtat försök till att revitalisera spärmen ledde till att de flesta orginal-spärmar numera inte existerar längre.

Detta projekt etablerades kort därefter och har två syften.

 1. Vara en de-facto digital ersättning för spexets fysiska Spärmar
 2. Vara en källa till historik över spexets mångåriga historia.

# Struktur

Projektet hostas på [Gihub pages](https://pages.github.com/).
Filen som servas är [index.html](https://github.com/vargladspexarna/vargladspexarna.github.io/blob/main/index.html "index.html")
index.html byggs upp utav scriptet [generateWebPage.py](https://github.com/vargladspexarna/vargladspexarna.github.io/blob/main/generateWebPage.py "generateWebPage.py") som tar en [mall](https://github.com/vargladspexarna/vargladspexarna.github.io/blob/main/pageTemplate.html "pageTemplate.html") och fyller ut den med låtar från mappen [sparmen](https://github.com/vargladspexarna/vargladspexarna.github.io/tree/main/sparmen "sparmen").

## Lägga till

För att lägga till en låt eller spex. Modifiera mappen [sparmen](https://github.com/vargladspexarna/vargladspexarna.github.io/tree/main/sparmen "sparmen").

**Mappstruktur**
 - Varje spex har sin egen mapp med ett eget nummer. 
 - Om ett spex har satts upp flera gånger har varje
   uppsättning sin egen undermapp med år och termin.
 - Varje låt har sin egen textfil

**Låtstruktur**
 - Varje låt har en titel och melodi som första stycke
 - Texten är radbruten för att göra det enklare att sjunga
 
> <b>Kålossal svanesång</b>
>
>  Melodi: Havet är Djupt

>     Allt verkar gå åt skogen
>     För chifen är en tyrann,
>     Han tycker min tid är mogen
>     En mardröm som blivit sann

## Regenerera Spärmen

För att regenerera spärmen och få in ändringar. Kör scriptet [generateWebPage.py](https://github.com/vargladspexarna/vargladspexarna.github.io/blob/main/generateWebPage.py "generateWebPage.py") lokalt med Python och commita den uppdaterade index.html filen.

Om du inte har python på din dator behöver du installera det.

## Tack
Tack för att du hjälper Var GladSpexarna bevara sin historia!
