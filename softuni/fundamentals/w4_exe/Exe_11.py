def loading_bar(percent):
    bars = percent // 10
    dots = 10 - bars
    if percent == 100:
        final_bar = f"{percent}% Complete!"
        final_bar += f"\n[{'%' * bars}{'.' * dots}]"
    else:
        final_bar = f"{percent}% [{'%' * bars}{'.' * dots}]"
        final_bar += "\nStill loading..."
    return final_bar

perc_input = int(input())
print(loading_bar(perc_input))