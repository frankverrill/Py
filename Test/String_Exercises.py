# String Exercies

poem_title = "spring storm"
poem_author = "William Carlos Williams"

# title() function
poem_title = "  preserve the verse  "
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

# upper() function
poem_author = "Frank Verrill"
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

# split() function
line_one = "The sky has given over"
line_one = "Spring Storm by William Carlos Williams"
line_one_words = line_one.split()
print(line_one_words)

# user split() to retrieve the last name in list of authors
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split()

print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# split() function
line_one = "The sky has given over"
line_one = "Spring Storm by William Carlos Williams"
line_one_words = line_one.split()
print(line_one_words)

# split() function
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, ",
"Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, ",
"Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# split() function used to create list of last author_last_names
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,",
"An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,",
"Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# Use split() function to parse lines of try:
spring_storm_text = \
    """The sky has given over\n 
its bitterness.\n 
Out of the dark change\n 
all day long\n 
rain falls and falls\n 
as if it would never end.\n
Still the snow keeps\n 
its hold on the ground.\n 
But water, water\n 
from a thousand runnels!\n 
It collects swiftly,\n 
dappled with black\n 
cuts a way for itself\n 
through green ice in the gutters.\n  
Drop after drop it falls\n  
from the withered grass-stems\n  
of the overhanging embankment.\n"""

spring_storm_lines = spring_storm_text.split("\n")

print(spring_storm_lines)
