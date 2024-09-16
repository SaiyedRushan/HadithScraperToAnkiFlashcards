import genanki

my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',  # Front of the card
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # Back of the card
    }
  ])

# Create a deck
my_deck = genanki.Deck(
  2059400110,
  'Hadiths on Good Manners and Form (Al-Adab)'
)

def add_hadiths_to_deck(hadiths):
  for chapter in hadiths:
    note = genanki.Note(
      model=my_model,
      fields=[chapter, '<br><br>'.join(hadith + '<br><br>' for hadith in hadiths[chapter])]
    )
    my_deck.add_note(note)

def generate_package():
  genanki.Package(my_deck).write_to_file('hadiths_on_good_manners_and_form.apkg')
