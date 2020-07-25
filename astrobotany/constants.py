STAGE_CUTOFFS = [
    (3600 * 24) * 0,
    (3600 * 24) * 1,
    (3600 * 24) * 3,
    (3600 * 24) * 10,
    (3600 * 24) * 20,
    (3600 * 24) * 30,
]

STAGES = ["seed", "seedling", "young", "mature", "flowering", "seed-bearing"]

STAGE_DESCRIPTIONS = {
    0: [
        "You're excited about your new seed.",
        "You wonder what kind of plant your seed will grow into.",
        "You're ready for a new start with this plant.",
        "You're tired of waiting for your seed to grow.",
        "You wish your seed could tell you what it needs.",
        "You can feel the spirit inside your seed.",
        "These pretzels are making you thirsty.",
        "Way to plant, Ann!",
        "'To see things in the seed, that is genius' - Lao Tzu",
    ],
    1: [
        "The seedling fills you with hope.",
        "The seedling shakes in the wind.",
        "You can make out a tiny leaf - or is that a thorn?",
        "You can feel the seedling looking back at you.",
        "You blow a kiss to your seedling.",
        "You think about all the seedlings who came before it.",
        "You and your seedling make a great team.",
        "Your seedling grows slowly and quietly.",
        "You meditate on the paths your plant's life could take.",
    ],
    2: [
        "The {species} makes you feel relaxed.",
        "You sing a song to your {species}.",
        "You quietly sit with your {species} for a few minutes.",
        "Your {species} looks pretty good.",
        "You play loud techno to your {species}.",
        "You play piano to your {species}.",
        "You play rap music to your {species}.",
        "You whistle a tune to your {species}.",
        "You read a poem to your {species}.",
        "You tell a secret to your {species}.",
        "You play your favorite record for your {species}.",
    ],
    3: [
        "Your {species} is growing nicely!",
        "You're proud of the dedication it took to grow your {species}.",
        "You take a deep breath with your {species}.",
        "You think of all the words that rhyme with {species}.",
        "The {species} looks full of life.",
        "The {species} inspires you.",
        "Your {species} makes you forget about your problems.",
        "Your {species} gives you a reason to keep going.",
        "Looking at your {species} helps you focus on what matters.",
        "You think about how nice this {species} looks here.",
        "The buds of your {species} might bloom soon.",
    ],
    4: [
        "The {color} flowers look nice on your {species}!",
        "The {color} flowers have bloomed and fill you with positivity.",
        "The {color} flowers remind you of your childhood.",
        "The {color} flowers remind you of spring mornings.",
        "The {color} flowers remind you of a forgotten memory.",
        "The {color} flowers remind you of your happy place.",
        "The aroma of the {color} flowers energize you.",
        "The {species} has grown beautiful {color} flowers.",
        "The {color} petals remind you of that favorite shirt you lost.",
        "The {color} flowers remind you of your crush.",
        "You smell the {color} flowers and are filled with peace.",
    ],
    5: [
        "You fondly remember the time you spent caring for your {species}.",
        "Seed pods have grown on your {species}.",
        "You feel like your {species} appreciates your care.",
        "The {species} fills you with love.",
        "You're ready for whatever comes after your {species}.",
        "You're excited to start growing your next plant.",
        "You reflect on when your {species} was just a seedling.",
        "You grow nostalgic about the early days with your {species}.",
    ],
    99: [
        "You wish you had taken better care of your plant.",
        "If only you had watered your plant more often..",
        "Your plant is dead, there's always next time.",
        "You cry over the withered leaves of your plant.",
        "Your plant died. Maybe you need a fresh start.",
    ],
}

COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
    "white",
    "black",
    "gold",
    "rainbow",
]

COLOR_MAP = {name: i for i, name in enumerate(COLORS)}

COLORS_PLAIN = COLORS[:-1]

SPECIES = [
    "poppy",
    "cactus",
    "aloe",
    "venus flytrap",
    "jade plant",
    "fern",
    "daffodil",
    "sunflower",
    "baobab",
    "lithops",
    "hemp",
    "pansy",
    "iris",
    "agave",
    "ficus",
    "moss",
    "sage",
    "snapdragon",
    "columbine",
    "brugmansia",
    "palm",
    "pachypodium",
]

RARITIES = ["common", "uncommon", "rare", "legendary", "godly"]

MUTATIONS = [
    "humming",
    "noxious",
    "vorpal",
    "glowing",
    "electric",
    "icy",
    "flaming",
    "psychic",
    "screaming",
    "chaotic",
    "hissing",
    "gelatinous",
    "deformed",
    "shaggy",
    "scaly",
    "depressed",
    "anxious",
    "metallic",
    "glossy",
    "psychedelic",
    "bonsai",
    "foamy",
    "singing",
    "fractal",
    "crunchy",
    "goth",
    "oozing",
    "stinky",
    "aromatic",
    "juicy",
    "smug",
    "vibrating",
    "lithe",
    "chalky",
    "naive",
    "ersatz",
    "disco",
    "levitating",
    "colossal",
    "luminous",
    "cosmic",
    "ethereal",
    "cursed",
    "buff",
    "narcotic",
    "gnu/linux",
    "abraxan",  # rip dear friend
]

WELCOME_SUBJECT = "Welcome to Astrobotany!"

WELCOME_MESSAGE = r"""
Greetings {name},

Welcome to astrobotany! You are visitor number {number}.

Please enjoy poking around this little app as a demonstration of what gemini:// is capable of.

Remember, YOU are what makes this community special. Always be true to yourself.

You can report any bugs that you encounter on the project issue tracker:
=>https://github.com/michael-lazar/astrobotany/issues

```
                  .' '.            __
         .        .   .           (__\_
          .         .         . -{{_(|8)
  jgs       ' .  . ' ' .  . '     (__/`
```

Your garden awaits,
admin
""".strip()
