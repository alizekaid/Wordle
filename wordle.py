import sys

if len(sys.argv[1]) != 5:   #This line provides that the WoD has 5 letters.
    print("The length of WoD must be five!")
    exit()

keyword = sys.argv[1]
for i in range(6):  #Provides that the given rights to test the predictions are 6.
    word = input(f"{i+1}.")
    print(f"Try{i+1} ({word}):", end=' ')

    if len(word) == 5 and word != keyword:  #Specifies the case that the length of word we tried is 5 letters, but it is not the WoD.

        print()
        for index in range(len(word)):
            if word[index] == keyword[index]:   #Indicates that the letters in the content of the tried word are compatible with the WoD and in the correct positions.
                print(f"{index+1}. letter exists and located in right position.")
            elif word[index] in keyword :   #Specifies the case that the letters in the tested word are are correct but their positions are incorrect.
                print(f"{index+1}. letter exists but located in wrong position.")
            else:   #Specifies the case that the letters in the tested word are not found in WoD.
                print(f"{index+1}. letter does not exist.")
    elif len(word) != 5:    #Specifies the case that the length of the tried word different than 5.

        print(f"The length of word must be five!")
    else:   #Specifies the case that when the WoD guessed right, it guessed right at which try.

        ordinals = ["st", "nd", "rd", "th", "th", "th"]
        print(f"Congratulations! You guess right in {i+1}{ordinals[i]} shot!\n")
        exit()
    print()
print("You are failed!\n")  #Prints the failure situation when the tried word didn't match with WoD after 6 tries.
exit()