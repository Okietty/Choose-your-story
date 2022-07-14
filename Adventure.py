action = input(
    "  Opening: Its late, 6:00 PM, you and three other pals are riding your bikes around the neighbourhood and pass by a creepy abandoned house, you all freeze because you all begin hearing whispers coming from it. The voice you hear sound so fimilar, almost asthough its someone close to you calling you to come closer. Do you go near?...... type yes/no ")

if action == "yes":
    print("  You all get closer, looking around the house and see something moving from the window.")

    action = input(
        "  One of your friends, being the genius that he is, dares everyone to go in the house, calling you a names for hesitating, do you give in and walk inside?....... type yes/no ")

    if action == "yes":
        print(
            "  Slowly walking in, you see many bugs and feel creeped out, the do slams shut behind you and you all try to pry it open escept for one with freaking out right now. Yo hear foot steps from the stairs and try to hide........ From an outsider's perspective, a scream can be heard coming from the house..... But no one comes out.")

    else:
        print(
            "  You all ignore the whispers and continue to ride your bikes to one of the friend's house for a sleep over.")

        action = input(
            "  Riding home, one of your friends hear a voice coming from the woods, they say its the same one they hear when assing by the house beofre. They say its calling to them, it shoulds like their sister, he couldn't resist and rushed to see if its her. Do you run after him?....... type yes/no ")

        if action == "yes":
            print(
                "  You all chase after him, telling him to slow down. You all run for a while. A scream is heard coming from the woods by the house in front of it. An angry man comes out thinking it was some kids causing him a ruckess, so he waits for the kids to come out. But they never did.")
        else:
            print(
                "  You argue they shouldn't but one fo the others, who's actually the one who run in the woods' brother rush and so did the other friend with you and so you thought you didn't want to stay out alone and so go in with them.")

elif action == "no":
    print(
        "  You'll all ignore the whispers and continue to ride your bikes to one of the friend's house for a sleep over.")

    action = input(
        "  Riding home, one of your friends hear a voice coming from the woods, they say its the same one they hear when assing by the house beofre. They say its calling to them, it shoulds like their sister, he couldn't resist and rushed to see if its her. Do you run after him?....... type yes/no ")

    if action == "yes":
        print(
            "  You all chase after him, telling him to slow down. You all run for a while. A scream is heard coming from the woods by the house in front of it. An angry man comes out thinking it was some kids causing him a ruckess, so he waits for the kids to come out. But they never did.")
    else:
        print(
            "  You argue they shouldn't but one fo the others, who's actually the one who run in the woods' brother rush and so did the other friend with you and so you thought you didn't want to stay out alone and so go in with them.")

else:
    print("Please type in all lowercase or choose one of the availble options.")
    print("Try again!")
