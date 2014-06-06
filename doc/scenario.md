100s at (0, 100) appears Fairy which moves to (100, 500) and attacks with aimed RedFireball
200s at (10, 100) appears Hoblin which moves to (200, 500) and attacks with linear Pellet at angle 90 and speed 300
300s at (10, 100) appears Raven which moves to (200, 500) and attacks with radial PurplePlasmaball at 4 directions and speed 100



300s Raven appears at (10,100) and moves linear(angle=0, speed=300) and attacks with simple Pellet



300s:
    Fairy:
        appears: (100, 500)
        moves: {100s: linear(90, 100), 200s: wait, 400s: linear (0, 200)}
        attacks: (aimed, RedFireball, (from 100s every 10s)) ИЛИ (linear(0, 700), Pellet, (at (200s, 300s, 400s, 800s))
