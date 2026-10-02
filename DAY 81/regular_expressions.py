import re

# pattern = "was"
pattern = r"[A-Z]+ink"

text = '''
The Kaiser class was a class of ships which were built in Germany prior to World War I and served in the Kaiserliche Marine. It was the third class of German dreadnoughts, and the first to feature turbine engines and superfiring turrets. The five ships were Kaiser (pictured), Friedrich der Grosse, Kaiserin, Prinzregent Luitpold, and König Albert. All five saw action in the North Sea during the war; they served together as VI Division of III Battle Squadron. Four were present during the Battle of Jutland. The ships also took part in Operation Albion in the Baltic Sea; during the operation, they were reorganized as IV Battle Zink Pink Sink Tink Link Squadron, under the command of Vice Admiral Wilhelm Souchon. At the end of the war, all five ships were interned at the British naval base in Scapa Flow. On 21 June 1919, they were scuttled to prevent their seizure by the Royal Navy. The ships were subsequently raised and broken up for scrap between 1929 and 1937. (This article is part of a featured topic: Battleships of Germany.)
'''

# match = re.search(pattern , text)
# print(match)

matches = re.finditer(pattern , text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])