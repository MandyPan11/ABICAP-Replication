import networkx as nx

# ============================================================
# 1. Graph definition (KCs, edges)
# ============================================================

def build_kidney_graph():
    G = nx.Graph()

    # ---------- Node data ----------
    kc = {
        # Basic structure and core functions
        "KC1":  {"label": "The kidneys are a pair of bean-shaped organs just above the waist",
                 "group": "Structure & core functions"},
        "KC2":  {"label": "The kidneys have many functions in the body",
                 "group": "Structure & core functions"},
        "KC3":  {"label": "The kidneys produce hormones",
                 "group": "Structure & core functions"},
        "KC4":  {"label": "The kidneys absorb minerals",
                 "group": "Structure & core functions"},
        "KC5":  {"label": "The kidneys filter blood",
                 "group": "Structure & core functions"},
        "KC6":  {"label": "The kidneys produce urine",
                 "group": "Structure & core functions"},

        # Waste and urine handling
        "KC7":  {"label": "Urine is the liquid waste product of the body",
                 "group": "Waste & urine"},
        "KC8":  {"label": "Wastes in the blood come from normal tissue breakdown and from food",
                 "group": "Waste & urine"},
        "KC9":  {"label": "After nutrients are taken from food, some wastes enter the blood",
                 "group": "Waste & urine"},
        "KC10": {"label": "If the kidneys did not remove these wastes, they would build up and damage the body",
                 "group": "Waste & urine"},
        "KC11": {"label": "The actual removal of wastes from the blood happens in nephrons",
                 "group": "Waste & urine"},

        # Hormones and regulation
        "KC12": {"label": "The kidneys secrete hormones that help maintain homeostasis",
                 "group": "Hormonal regulation"},
        "KC13": {"label": "Erythropoietin stimulates bone marrow to produce red blood cells when more are needed",
                 "group": "Hormonal regulation"},
        "KC14": {"label": "The kidneys secrete renin, which regulates blood pressure",
                 "group": "Hormonal regulation"},
        "KC15": {"label": "The kidneys secrete calcitriol (active vitamin D), which helps maintain calcium for bones",
                 "group": "Hormonal regulation"},
        "KC16": {"label": "The kidneys themselves are also regulated by hormones",
                 "group": "Hormonal regulation"},
        "KC17": {"label": "Antidiuretic hormone from the hypothalamus makes the kidneys produce more concentrated urine when the body is low on water",
                 "group": "Hormonal regulation"},

        # Homeostasis roles (water, RBCs, blood pressure)
        "KC18": {"label": "The kidneys help maintain the body's water level",
                 "group": "Homeostasis roles"},
        "KC19": {"label": "The kidneys help regulate red blood cell levels",
                 "group": "Homeostasis roles"},
        "KC20": {"label": "The kidneys help regulate blood pressure",
                 "group": "Homeostasis roles"},
        "KC21": {"label": "The kidneys react to changes in the body's water level throughout the day",
                 "group": "Homeostasis roles"},
        "KC22": {"label": "When water intake decreases, the kidneys keep more water in the body instead of letting it leave in urine",
                 "group": "Homeostasis roles"},
        "KC23": {"label": "The kidneys need constant pressure to filter the blood",
                 "group": "Homeostasis roles"},
        "KC24": {"label": "When blood pressure drops too low, the kidneys increase the pressure by producing angiotensin",
                 "group": "Homeostasis roles"},
        "KC25": {"label": "Angiotensin is a blood vessel-constricting protein",
                 "group": "Homeostasis roles"},
    }

    for k, attrs in kc.items():
        G.add_node(k, **attrs)

    # ---------- Edge data ----------
    base_w = {
        "supports": 0.5,
        "has_examples": 0.5,
        "explains": 0.5,
        "leads_to": 0.5,
        "prevents": 0.5,
        "defines_mechanism_for": 0.5,
        "provides_context_for": 0.5,
        "modifies": 0.5,
        "defined_by": 0.5,
    }

    edges = [
        # Kidney location and general function
        ("KC1", "KC2", "supports"),
        ("KC2", "KC3", "has_examples"),
        ("KC2", "KC4", "has_examples"),
        ("KC2", "KC5", "has_examples"),
        ("KC2", "KC6", "has_examples"),

        # Urine and waste handling
        ("KC6", "KC7", "explains"),
        ("KC8", "KC9", "supports"),
        ("KC8", "KC10", "explains"),
        ("KC9", "KC10", "leads_to"),
        ("KC5", "KC10", "prevents"),
        ("KC11", "KC5", "defines_mechanism_for"),
        ("KC11", "KC10", "explains"),

        # Hormones and homeostasis
        ("KC12", "KC3", "supports"),
        ("KC12", "KC13", "provides_context_for"),
        ("KC12", "KC14", "provides_context_for"),
        ("KC12", "KC15", "provides_context_for"),

        ("KC13", "KC19", "supports"),
        ("KC13", "KC12", "explains"),

        ("KC14", "KC20", "supports"),
        ("KC14", "KC12", "explains"),

        ("KC15", "KC12", "explains"),

        # Hormonal regulation of kidneys
        ("KC16", "KC17", "provides_context_for"),
        ("KC17", "KC18", "supports"),
        ("KC17", "KC22", "supports"),
        ("KC17", "KC6", "modifies"),

        # Water level, RBC level, blood pressure
        ("KC18", "KC21", "provides_context_for"),
        ("KC21", "KC22", "leads_to"),
        ("KC22", "KC18", "supports"),

        ("KC19", "KC13", "defined_by"),
        ("KC19", "KC12", "supports"),

        ("KC20", "KC14", "defined_by"),
        ("KC20", "KC23", "provides_context_for"),

        # Filtration and blood pressure
        ("KC23", "KC5", "defines_mechanism_for"),
        ("KC23", "KC24", "provides_context_for"),

        ("KC24", "KC25", "defined_by"),
        ("KC24", "KC20", "supports"),
        ("KC24", "KC23", "supports"),

        ("KC25", "KC24", "explains"),
        ("KC25", "KC20", "supports"),
    ]

    for u, v, rel in edges:
        G.add_edge(u, v, relation=rel, weight=base_w[rel])

    return G


def build_graph():
    return build_kidney_graph()

# Paragraph → KC mapping
PARA = {
    1: ["KC1","KC2","KC3","KC4","KC5","KC6"],
    2: ["KC7","KC8","KC9","KC10","KC11"],
    3: ["KC12","KC13","KC14","KC15","KC16","KC17"],
    4: ["KC18","KC19","KC20","KC21","KC22","KC23","KC24","KC25"],
}

# Fact-question KC coverage
FACT_KCS = {
    "KC17","KC7","KC9","KC11","KC24","KC25","KC12","KC13"
}

# Inference items
INF_ITEMS = [
    {"name": "Inf1_ConcentratedUrine_WaterConservation",
    "kcs": {"KC17","KC22"}},
    {"name": "Inf2_DigestionWaste_NephronsFilter",
    "kcs": {"KC9","KC11"}},
    {"name": "Inf3_VesselConstrict_BPIncrease",
    "kcs": {"KC24","KC25"}},
    {"name": "Inf4_RBCs_ForHomeostasis",
    "kcs": {"KC12","KC13"}},
]

NUM_FACT = len(FACT_KCS)
NUM_INF  = len(INF_ITEMS)
