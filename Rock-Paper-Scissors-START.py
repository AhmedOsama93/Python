#Ahmed Osama Mahmoud FCAI cairo univ

import random as rd;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Choose your Weapon:")

print("1-Rock.                2-Paper.                3-Scissors.");

weapons=[rock , paper , scissors];
weaponsName=[" Rock" , " Paper" , " Scissors"];

choose = int(input());
pc_choose = rd.randint(1,len(weapons));

print("Your Choose:" + weaponsName[choose-1])
print(weapons[int(choose)])

print("PC Choose:"+ weaponsName[pc_choose-1])

print(weapons[pc_choose-1])


if choose == pc_choose:
    print("It's draw");
elif choose == 3 and pc_choose==1:
    print("You lose!");
elif choose == 2 and pc_choose==3:
    print("You lose!");
elif choose == 1 and pc_choose==2:
    print("You lose!");
    
else: print("You Win!");        
    
    
