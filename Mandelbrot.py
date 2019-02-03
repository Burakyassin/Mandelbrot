import graphics

# Gebruik getal tussen -1 en 1
# Vergeet niet om de schaal en de offset van het venster te veranderen

# Probeer: randomiser = -0.5 & y_offset = 1.134597252 & x_offset = 0.52565809

randomiser = 1
precision = 100
win_max = 300
scale = 1000
get_x = 0
get_y = 0
y_offset = 0
x_offset = 0

# Maakt een Graphisch venster met de naam "Mandelbrot", de grootte wordt bepaald door de variabel 'win_max'
win = graphics.GraphWin("Mandelbrot", win_max, win_max)

# Herhaalt de grootte van het venster
for num_y in range(0, win_max + 1):
    
    # Deze vergelijking wordt gebruikt zodat het programma een offset en een schaal krijgt voor de de waarde van y
    y = (num_y/(scale)) - ((win_max/2)/scale) + y_offset

    # Herhaalt opnieuw de grootte van het venster voor elke pixel 300 * 300
    for num_x in range(0, win_max + 1):

        # Controleert en telt elke pixel in het venster
        count = 0
        check = 0

        # Deze vergelijking wordt gebruikt zodat het programma een offset en een schaal krijgt voor de de waarde van x
        x = (num_x/(scale)) - ((win_max/2)/scale) + x_offset

        # Deze vergelijking wordt gebruikt om de grootte van het 'punt' te bepalen, nodig voor if statement later in het script
        z = complex(x,y)**2 - randomiser

        # Voert de while-lus zo vaak uit als is vastgesteld
        while count < precision:

            # Gebruikt de geïmporteerde 'graphics' module om een punt te maken op x = num_x & y = num_Y
            point = graphics.Point(num_x, num_y)

            # Deze vergelijking wort constant herhaalt om steeds een nieuwe waarde voor z te krijgen 
            z = z**2 - randomiser

            # Deze waarde heeft effect op de precision, verhoog voor een betere Mandelbrot (voorzichtig, want je veranderd de kleuren)
            if abs(z) > 1000000000000:

                # Bewaart het aantal tellingen om de waarde voor de precision te bereiken
                check = count
                
                # Count = precision, zorgt ervoor dat de while-lus wordt gebroken
                count = precision

            # Update de while-lus, totdat de precision wordt bereikt
            count += 1
            
        # Deze eerste waarde wordt gebruikt om de eerste kleur van de Mandelbrot te bepalen
        if abs(z) <= 1:
            point.setFill("white")

        # Deze kleuren hebben effect op de punten door de snelheid van de veranderende punten
        # door de herhaling van de vergelijking van de waarde van z
        # These colors effect points by how quickly point escapes using the iteration
        elif check > 27:
            point.setFill("purple")           
            
        elif check > 21:
            point.setFill("pink")           
            
        elif check > 19:
            point.setFill("red")
            
        elif check > 17:
            point.setFill("orange")

        elif check > 15:
            point.setFill("yellow")

        elif check > 13:
            point.setFill("green")    
            
        elif check > 11:
            point.setFill("blue")
            
        elif check > 9:
            point.setFill("indigo")
            
        elif check > 7:
            point.setFill("violet")

        elif check > 5:
            point.setFill("black")
            
        elif check > 4:
            point.setFill("cyan")

        else:
            point.setFill("turquoise")

        point.draw(win)

#Het invoegen van een zoom functie is helaas niet gelukt, maar dit wilde we wel doen
#Misschien kan jij ons stukje code verbeteren waardoor het wel lukt, Hugo
"""
while True:
    
    get_mouse = win.getMouse()

    get_x += 150 - get_mouse.getX()
    get_y += -150 + get_mouse.getY()
    scale *= 2
    win.close()

    win = graphics.GraphWin("Mandelbrot", win_max, win_max)

    for num_x in range(0, win_max + 1):  
        y = ((get_y + (get_x - num_y/(scale))) - ((win_max/2)/scale)) + y_offset
        point = graphics.Point(x, y)
"""