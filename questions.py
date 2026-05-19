# Each option has a score 1-4 on its dimension (1=right/conservative, 4=left/progressive)
# Dimensions: eco | econ | ukraine | police

QUESTIONS = [
    # ── SECTION 1: Environment & Eco-Activism ─────────────────────────────────
    {
        "id": "eco_activism",
        "section": "environment",
        "section_label": "Environment & Eco-Activism",
        "icon": "🌍",
        "number": 1,
        "text": (
            "How do you view organizations like Extinction Rebellion, "
            "Soulèvements de la Terre, and Les Amis de la Terre?"
        ),
        "context": (
            "In June 2023 the Borne government issued a dissolution decree against "
            "Soulèvements de la Terre, calling it an eco-terrorist organization. "
            "The Conseil d'État suspended the decree two months later."
        ),
        "references": [
            {
                "label": "Decree dissolving SdlT — Journal Officiel 21 juin 2023",
                "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047688246",
            },
            {
                "label": "Conseil d'État suspension — 9 août 2023",
                "url": "https://www.conseil-etat.fr/actualites/le-conseil-d-etat-suspend-la-dissolution-des-soulevements-de-la-terre",
            },
        ],
        "dimension": "eco",
        "options": [
            {
                "value": "terrorist",
                "label": "Eco-terrorists — their illegal actions harm the environmental cause and should be prosecuted",
                "score": 1,
            },
            {
                "value": "radical",
                "label": "Too radical — I understand the frustration but civil disobedience alienates public opinion",
                "score": 2,
            },
            {
                "value": "necessary",
                "label": "Legitimate civil disobedience — blocking pipelines and construction sites is justified when politics fails",
                "score": 3,
            },
            {
                "value": "vanguard",
                "label": "The vanguard of the ecological struggle — they don't go far enough given the urgency",
                "score": 4,
            },
        ],
    },
    {
        "id": "eco_economy",
        "section": "environment",
        "section_label": "Environment & Eco-Activism",
        "icon": "⚡",
        "number": 2,
        "text": "France's economic model in the face of climate change should be:",
        "context": (
            "The notion of 'plancher écologique et plafond social' (doughnut economics) "
            "was referenced in AN debates on the SNBC (Stratégie Nationale Bas-Carbone). "
            "France missed its 2020 carbon budget by 2.5%. "
            "Capitalism's growth imperative is the core fault line dividing the green left from green techno-optimists."
        ),
        "references": [
            {
                "label": "Loi Énergie-Climat 2019 (SNBC & objectifs carbone)",
                "url": "https://www.legifrance.gouv.fr/loda/id/LEGIARTI000042792543",
            },
            {
                "label": "Rapport du Haut Conseil pour le Climat 2023",
                "url": "https://www.hautconseilclimat.fr/publications/rapport-annuel-2023-acter-lexigence/",
            },
        ],
        "dimension": "eco",
        "options": [
            {
                "value": "growth",
                "label": "Unlimited growth — innovation and green tech will solve climate change without sacrificing prosperity",
                "score": 1,
            },
            {
                "value": "green_growth",
                "label": "Green growth — decouple carbon emissions from GDP through strong carbon pricing and R&D investment",
                "score": 2,
            },
            {
                "value": "selective_degrowth",
                "label": "Selective degrowth — radically shrink harmful sectors (aviation, SUVs, fast fashion) while growing others",
                "score": 3,
            },
            {
                "value": "degrowth",
                "label": "Degrowth (décroissance) — the capitalist growth paradigm is structurally incompatible with planetary limits",
                "score": 4,
            },
        ],
    },
    # ── SECTION 2: Social Inequalities, Feminism & Class ──────────────────────
    {
        "id": "wealth_tax",
        "section": "inequalities",
        "section_label": "Social Inequalities, Feminism & Class",
        "icon": "⚖️",
        "number": 3,
        "text": (
            "On Gabriel Zucman's proposal for a 2% global minimum tax on billionaires' "
            "net fortunes (endorsed by the G20 in 2024, championed by France's presidency):"
        ),
        "context": (
            "France led the G20 push under Macron in 2024. LFI went further with 90% top marginal rates; "
            "Renaissance supported the G20 framework; LR and RN opposed it as 'confiscatory'. "
            "The ISF (wealth tax) was abolished by Macron in 2018, replaced by the IFI (immovable property only). "
            "Oxfam France: the 500 richest French individuals own more than the poorest 40% combined."
        ),
        "references": [
            {
                "label": "Suppression de l'ISF — Loi de finances 2018, Legifrance",
                "url": "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036339197",
            },
            {
                "label": "Rapport Zucman — EU Tax Observatory 2024",
                "url": "https://www.taxobservatory.eu/publication/a-blueprint-for-a-coordinated-minimum-effective-taxation-standard-for-ultra-high-net-worth-individuals/",
            },
            {
                "label": "Débat AN sur la réforme fiscale — Novembre 2024",
                "url": "https://www.assemblee-nationale.fr/dyn/17/dossiers/alt/plfss_2025",
            },
        ],
        "dimension": "econ",
        "options": [
            {
                "value": "zucman_plus",
                "label": "France should go further: restore the ISF, 90% top marginal tax, unilateral implementation if needed",
                "score": 4,
            },
            {
                "value": "zucman_support",
                "label": "I fully support the 2% Zucman Tax through international coordination — the G20 framework is a good start",
                "score": 3,
            },
            {
                "value": "zucman_skeptic",
                "label": "Better to tax income and consumption — wealth taxes cause capital flight and are difficult to enforce",
                "score": 2,
            },
            {
                "value": "trickle_down",
                "label": "The rich already pay too much — lowering taxes on capital creates investment and jobs for everyone (trickle-down)",
                "score": 1,
            },
        ],
    },
    {
        "id": "intersectionality",
        "section": "inequalities",
        "section_label": "Social Inequalities, Feminism & Class",
        "icon": "✊",
        "number": 4,
        "text": (
            "Which best describes your view on the relationship between ecology, feminism, and class struggle?"
        ),
        "context": (
            "'L'écologie sans féminisme et sans lutte des classes, c'est du jardinage' is a slogan "
            "associated with eco-socialist and feminist movements in France. "
            "The battle lines: LFI and EELV embrace intersectionality; RN opposes it as 'woke ideology'; "
            "the left itself is divided (class-first Chevènementistes vs. intersectional socialists). "
            "French women earn on average 24% less than men (INSEE 2023). "
            "The right to abortion (IVG) was constitutionalized in March 2024 — voted by 780 to 72 at the Congrès."
        ),
        "references": [
            {
                "label": "Constitutionnalisation de l'IVG — Loi constitutionnelle 4 mars 2024",
                "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049282977",
            },
            {
                "label": "INSEE — Écarts de salaire femmes-hommes 2023",
                "url": "https://www.insee.fr/fr/statistiques/7762736",
            },
        ],
        "dimension": "econ",
        "options": [
            {
                "value": "intersectional",
                "label": "'Ecology without feminism and class struggle is just gardening' — these struggles are inseparable",
                "score": 4,
            },
            {
                "value": "parallel",
                "label": "All three causes are important but require distinct strategies — don't conflate them",
                "score": 3,
            },
            {
                "value": "class_first",
                "label": "Class struggle is primary — identity politics fragment the working class and serve the ruling order",
                "score": 2,
            },
            {
                "value": "traditional",
                "label": "Traditional family values and national cohesion offer better social stability than these ideological frameworks",
                "score": 1,
            },
        ],
    },
    # ── SECTION 3: Support to Ukraine ─────────────────────────────────────────
    {
        "id": "ukraine_support",
        "section": "ukraine",
        "section_label": "Support to Ukraine",
        "icon": "🇺🇦",
        "number": 5,
        "text": "France's military and financial commitment to Ukraine should be:",
        "context": (
            "Macron caused controversy in February 2024 by refusing to rule out sending French troops to Ukraine. "
            "The Assemblée Nationale voted aid packages for Ukraine multiple times: LFI voted against several; "
            "RN abstained or voted against. The EU's EPF (European Peace Facility) has provided €6.1bn in military aid. "
            "France delivered AMX-10RC armored vehicles, SCALP missiles, and Caesar howitzers."
        ),
        "references": [
            {
                "label": "Vote AN — Soutien militaire à l'Ukraine (loi de programmation militaire)",
                "url": "https://www.assemblee-nationale.fr/dyn/16/dossiers/programmation_militaire_2024_2030",
            },
            {
                "label": "Résolution PE — Soutien à l'Ukraine, mars 2024",
                "url": "https://www.europarl.europa.eu/doceo/document/TA-9-2024-0172_FR.html",
            },
        ],
        "dimension": "ukraine",
        "options": [
            {
                "value": "troops",
                "label": "Send troops if necessary — Macron's open-door posture was right; security requires direct commitment",
                "score": 4,
            },
            {
                "value": "weapons",
                "label": "Continue weapons and financial support — no troops but full commitment to Ukrainian victory",
                "score": 3,
            },
            {
                "value": "humanitarian",
                "label": "Limit to humanitarian aid and diplomacy — push for negotiations to end the bloodshed now",
                "score": 2,
            },
            {
                "value": "no_support",
                "label": "Stop all support — France is being dragged into a US/NATO proxy war that threatens European security",
                "score": 1,
            },
        ],
    },
    {
        "id": "ukraine_origins",
        "section": "ukraine",
        "section_label": "Support to Ukraine",
        "icon": "🌐",
        "number": 6,
        "text": "The war in Ukraine primarily resulted from:",
        "context": (
            "This question distinguishes genuine geopolitical analysis from Russian-aligned propaganda narratives. "
            "Mélenchon/LFI positioned the conflict as a NATO provocation (Maidan framing); "
            "Zemmour and parts of RN echoed Russian talking points. "
            "The EU and French government officially recognize the invasion as unprovoked under international law. "
            "The ICJ ruled in January 2025 that Russia violated the Genocide Convention's prohibition on incitement."
        ),
        "references": [
            {
                "label": "CIJ — Arrêt Ukraine c. Russie, janvier 2025",
                "url": "https://www.icj-cij.org/case/182",
            },
            {
                "label": "Résolution ONU ES-11/1 — Agression contre l'Ukraine (141 voix pour)",
                "url": "https://undocs.org/A/RES/ES-11/1",
            },
        ],
        "dimension": "ukraine",
        "options": [
            {
                "value": "illegal_invasion",
                "label": "Russia's illegal invasion of a sovereign state — a clear violation of the UN Charter and international law",
                "score": 4,
            },
            {
                "value": "nato_context",
                "label": "Russian aggression is unjustifiable, but NATO's eastward expansion created legitimate security concerns",
                "score": 3,
            },
            {
                "value": "nato_proxy",
                "label": "The US and NATO triggered the war through the 2014 Maidan coup and broken promises on NATO expansion",
                "score": 2,
            },
            {
                "value": "russia_defending",
                "label": "Russia is defending itself from NATO encirclement and the persecution of Russian speakers in eastern Ukraine",
                "score": 1,
            },
        ],
    },
    # ── SECTION 4: Police Violence & Systemic Racism ──────────────────────────
    {
        "id": "systemic_racism",
        "section": "police",
        "section_label": "Police Violence & Systemic Racism",
        "icon": "⚡",
        "number": 7,
        "text": (
            "Regarding police violence in France — the deaths of Adama Traoré (2016), "
            "Cédric Chouviat (2020), and Nahel M. (2023):"
        ),
        "context": (
            "Nahel Merzouk, 17, was shot by a police officer during a traffic stop in Nanterre on 27 June 2023 — "
            "sparking a week of riots. The IGPN (police oversight) opened 38 investigations into police conduct during the riots. "
            "France has been condemned by the ECHR multiple times for inhuman treatment by police. "
            "The term 'violences policières' was removed from an AN resolution draft under pressure from the right in 2021."
        ),
        "references": [
            {
                "label": "IGPN — Rapport annuel 2023 (usage des armes, plaintes)",
                "url": "https://www.interieur.gouv.fr/Publications/Rapports/IGPN-rapport-annuel-2023",
            },
            {
                "label": "ECHR — Saoud c. France (2007), violences policières",
                "url": "https://hudoc.echr.coe.int/eng#{%22itemid%22:[%22001-79572%22]}",
            },
            {
                "label": "Suppression de 'violences policières' — débat AN, jan. 2021",
                "url": "https://www.assemblee-nationale.fr/dyn/15/dossiers/securite_globale",
            },
        ],
        "dimension": "police",
        "options": [
            {
                "value": "systemic",
                "label": "Systemic racism exists in the French police — structural reform, independent oversight, and disarmament are necessary",
                "score": 4,
            },
            {
                "value": "isolated",
                "label": "Serious isolated cases of excessive force must be addressed, but the institution is not systemically racist",
                "score": 3,
            },
            {
                "value": "police_side",
                "label": "Police face impossible conditions — media coverage amplifies rare incidents and dangerously demoralizes officers",
                "score": 2,
            },
            {
                "value": "denial",
                "label": "The 'police violence' narrative is a politicized attack designed to destabilize the state and embolden criminals",
                "score": 1,
            },
        ],
    },
    {
        "id": "lbd_armament",
        "section": "police",
        "section_label": "Police Violence & Systemic Racism",
        "icon": "🛡️",
        "number": 8,
        "text": (
            "Regarding LBD (Lanceurs de Balles de Défense / Flash-Balls) and GLI-F4 grenades "
            "used by French police for crowd control:"
        ),
        "context": (
            "Since 2017 (Gilets Jaunes onwards), LBDs have caused 30+ eye losses, 5 deaths, and hundreds of severe injuries. "
            "France is one of the few EU countries that uses these weapons for crowd control. "
            "Amnesty International and the UN Human Rights Committee have called for their ban. "
            "The Sénat and AN have both rejected proposals to ban LBDs (2019, 2020, 2023). "
            "The Gilets Jaunes movement became the central political test case."
        ),
        "references": [
            {
                "label": "Proposition de loi interdisant le LBD — rejetée AN, fév. 2019",
                "url": "https://www.assemblee-nationale.fr/dyn/15/textes/l15b1667_proposition-loi",
            },
            {
                "label": "Amnesty International — Rapport maintien de l'ordre 2020",
                "url": "https://www.amnesty.fr/discriminations/actualites/maintien-de-lordre-france",
            },
        ],
        "dimension": "police",
        "options": [
            {
                "value": "ban_now",
                "label": "Ban immediately — 30+ people have lost eyes, 5 died; no crowd-control justification outweighs this",
                "score": 4,
            },
            {
                "value": "strict_rules",
                "label": "Keep with strict independent oversight — mandatory bodycams, public footage, accountability for misuse",
                "score": 3,
            },
            {
                "value": "maintain",
                "label": "Police need these tools to maintain order — restrict use protocols but don't disarm officers",
                "score": 2,
            },
            {
                "value": "more_force",
                "label": "Police should have even greater means — riots proved the state needs stronger tools to restore order",
                "score": 1,
            },
        ],
    },
    # ── CROSS-CUTTING Q9: State role (economic calibration) ───────────────────
    {
        "id": "state_role",
        "section": "cross",
        "section_label": "Cross-Cutting: The Role of the State",
        "icon": "🏛️",
        "number": 9,
        "text": "The primary role of the French state should be:",
        "context": (
            "This question maps the classic left–right divide on state intervention. "
            "It cross-validates Q3 (Zucman Tax) and Q7 (police). "
            "Note: the souverainiste right (RN) occupies a unique position — "
            "it wants a strong interventionist state for security and borders but opposes redistribution to 'non-nationals'. "
            "This is a classic inconsistency trap for RN voters who also claim social solidarity."
        ),
        "references": [
            {
                "label": "Programme NFP 2024 — nationalisations et ISF",
                "url": "https://www.assemblee-nationale.fr/dyn/17/organes/groupes/gauche",
            },
            {
                "label": "Programme Renaissance 2022 — réforme de l'État",
                "url": "https://programme-en-marche.fr",
            },
        ],
        "dimension": "econ",
        "options": [
            {
                "value": "planification",
                "label": "Plan and nationalize key sectors — guarantee universal housing, health, education, and tax capital aggressively",
                "score": 4,
            },
            {
                "value": "regulated_market",
                "label": "Regulate markets firmly — strong public services funded by progressive taxation, address market failures",
                "score": 3,
            },
            {
                "value": "limited_state",
                "label": "Streamline bureaucracy and lower taxes — markets drive growth better than state intervention",
                "score": 2,
            },
            {
                "value": "sovereign_state",
                "label": "Protect national borders and identity — strong security apparatus, but reduce redistribution for non-nationals",
                "score": 1,
            },
        ],
    },
    # ── CROSS-CUTTING Q10: Political alignment (troll trap + calibration) ──────
    {
        "id": "political_alignment",
        "section": "cross",
        "section_label": "Cross-Cutting: Political Alignment",
        "icon": "🗳️",
        "number": 10,
        "text": (
            "Which political family or candidate for 2027 is closest to your views?"
        ),
        "context": (
            "This calibration question cross-checks your declared political identity against "
            "the positions you expressed in Q1–Q9. A significant mismatch flags a potential inconsistency.\n\n"
            "Key distinctions to note:\n"
            "• Sandrine Rousseau (EELV radical) ≠ Yannick Jadot (EELV moderate) — "
            "Rousseau is degrowth+intersectional, Jadot is green-centrist; the 2027 Écologiste candidate is Marine Tondelier.\n"
            "• François Bayrou (MoDem, centrist PM, independent tradition) ≠ Gabriel Attal "
            "(Renaissance, right-leaning Macronist, ex-PM).\n"
            "• Ian Brossat is PCF (Communist Party), not LFI — he ran on the NFP list but belongs to the Communist current.\n"
            "• Fabien Roussel (PCF) and Jérôme Guedj (PS) are distinct from Glucksmann's centrist Place Publique."
        ),
        "references": [
            {
                "label": "LCP — Liste des 29 candidats déclarés ou prétendants 2027",
                "url": "https://lcp.fr/actualites/presidentielle-2027-la-liste-des-candidats-deja-en-lice-et-des-pretendants-436373",
            },
            {
                "label": "Résultats législatives 2024 — premier tour",
                "url": "https://www.interieur.gouv.fr/Elections/Les-resultats/Legislatives/elecresult__legislatives-2024",
            },
        ],
        "dimension": "calibration",
        "groups": [
            {"label": "── Extrême gauche", "values": ["arthaud", "autain", "poutou"]},
            {"label": "── Gauche radicale / LFI", "values": ["melenchon", "ruffin"]},
            {"label": "── PCF", "values": ["roussel", "brossat"]},
            {"label": "── PS", "values": ["guedj", "faure_vallaud", "hollande"]},
            {"label": "── Écologistes", "values": ["tondelier", "batho", "s_rousseau"]},
            {"label": "── Centre-gauche", "values": ["glucksmann", "cazeneuve"]},
            {"label": "── Centre", "values": ["bayrou", "e_philippe", "attal", "darmanin", "de_villepin"]},
            {"label": "── Droite", "values": ["retailleau", "bertrand", "lisnard", "dupont_aignan"]},
            {"label": "── Extrême droite", "values": ["le_pen", "zemmour", "philippot", "asselineau"]},
            {"label": "── Non-vote", "values": ["none"]},
        ],
        "options": [
            # ── Extrême gauche ────────────────────────────────────────────────
            {
                "value": "arthaud",
                "group": "Extrême gauche",
                "label": "Nathalie Arthaud — Lutte Ouvrière (LO)",
                "note": "Trotskyist, anti-imperialist. LO ran 554 independent candidates in 2022 and 2024, refusing both NUPES and NFP.",
                "refs": [
                    {"label": "LO on 2022 legislative independance from NUPES", "url": "https://www.lutte-ouvriere.org/mensuel/article/2022-06-26-lextreme-gauche-aux-elections-legislatives_367110.html"},
                    {"label": "Arthaud 2023 speech rejecting left-wing electoral compromises", "url": "https://www.lutte-ouvriere.org/portail/brochures/publications-brochures-fete-de-lutte-ouvriere-discours-de-nathalie-arthaud-dimanche-28-mai-692397.html"},
                ],
                "score": None,
            },
            {
                "value": "autain",
                "group": "Extrême gauche",
                "label": "Clémentine Autain — L'Après",
                "note": "Left the LFI parliamentary group in July 2024 (not 2023) along with Ruffin, Corbière. Eco-feminist, broader coalition strategy.",
                "refs": [
                    {"label": "Le JDD — Autain rompt avec LFI, juillet 2024", "url": "https://www.lejdd.fr/politique/legislatives-clementine-autain-rompt-avec-lfi-et-rejoint-le-groupe-des-purges-147303"},
                ],
                "score": None,
            },
            {
                "value": "poutou",
                "group": "Extrême gauche",
                "label": "Philippe Poutou / Olivier Besancenot — NPA",
                "note": "Poutou is a Ford factory worker and anti-capitalist worker candidate. Besancenot is the NPA's historic public face.",
                "refs": [
                    {"label": "Révolution Permanente — Poutou, ouvrier ex-candidat", "url": "https://www.revolutionpermanente.fr/Philippe-Poutou-ouvrier-ex-candidat-a-la-presidentielle-et-menace-de-licenciement"},
                    {"label": "Site officiel campagne Poutou 2022", "url": "https://poutou2022.org/node/4"},
                ],
                "score": None,
            },
            # ── LFI ──────────────────────────────────────────────────────────
            {
                "value": "melenchon",
                "group": "LFI",
                "label": "Jean-Luc Mélenchon — La France Insoumise",
                "note": "4th presidential candidacy. Programme: rupture with EU treaties ('Plan A/Plan B'). Ambiguous on NATO expansion in February 2022 speech to the AN.",
                "refs": [
                    {"label": "Le JDD — Plan B de Mélenchon expliqué", "url": "https://www.lejdd.fr/Politique/Europe-c-est-quoi-le-plan-B-de-Melenchon-858638"},
                    {"label": "LFI — Discours Mélenchon AN sur l'Ukraine, 28 fév. 2022", "url": "https://lafranceinsoumise.fr/2022/02/28/guerre-en-ukraine-intervention-de-jean-luc-melenchon-a-lassemblee-nationale/"},
                ],
                "score": None,
            },
            {
                "value": "ruffin",
                "group": "LFI",
                "label": "François Ruffin — Debout",
                "note": "Left the LFI parliamentary group in June–July 2024. Left-populist, more inclusive tone than Mélenchon. Running in the 2027 left primary.",
                "refs": [
                    {"label": "LCP — Ruffin: 's'il n'y a pas de primaire, moi j'y vais'", "url": "https://lcp.fr/actualites/presidentielle-2027-s-il-n-y-a-pas-de-primaire-moi-j-y-vais-annonce-francois-ruffin"},
                ],
                "score": None,
            },
            # ── PCF ──────────────────────────────────────────────────────────
            {
                "value": "roussel",
                "group": "PCF",
                "label": "Fabien Roussel — Parti Communiste Français (PCF)",
                "note": "'Joie de vivre communiste' was his 2022 campaign theme. More police-republican than LFI: defended proximity policing in 2021. Ambiguous on Ukraine (PCF historical ties to Russia).",
                "refs": [
                    {"label": "Le JDD — 'Le plaisir, c'est de gauche' (joie de vivre angle)", "url": "https://www.lejdd.fr/Politique/le-plaisir-cest-de-gauche-rencontre-avec-le-communiste-fabien-roussel-un-candidat-heureux-4097576"},
                    {"label": "Révolution Permanente — Roussel's pro-security positions", "url": "https://www.revolutionpermanente.fr/Repression-policiere-immigration-Roussel-enchaine-les-sorties-securitaires"},
                    {"label": "Roussel défend une 'police nationale de proximité' (2021)", "url": "http://www.communcommune.com/2021/05/droit-a-la-securite-fabien-roussel-pcf-defend-une-police-nationale-de-proximite.html"},
                ],
                "score": None,
            },
            {
                "value": "brossat",
                "group": "PCF",
                "label": "Ian Brossat — PCF",
                "note": "PCF senator for Paris since September 2023. Former deputy mayor of Paris for housing (2014–2023). Stronger on police reform and housing rights than Roussel.",
                "refs": [
                    {"label": "Sénat — Fiche Ian Brossat (PCF, Paris)", "url": "https://www.senat.fr/senateur/brossat_ian21088q.html"},
                    {"label": "Paris.fr — Profil Ian Brossat, adjoint au logement", "url": "https://www.paris.fr/pages/brossat-ian-2260"},
                ],
                "score": None,
            },
            # ── PS ───────────────────────────────────────────────────────────
            {
                "value": "guedj",
                "group": "PS",
                "label": "Jérôme Guedj — PS (aile gauche)",
                "note": "AN deputy for Essonne (6th constituency). Left flank of PS: social services, aging policy, anti-austerity. Member of Social Affairs commission.",
                "refs": [
                    {"label": "Assemblée nationale — Fiche Jérôme Guedj (Essonne, PS)", "url": "https://www.assemblee-nationale.fr/dyn/deputes/PA1567"},
                    {"label": "NosDéputés — profil et votes Jérôme Guedj", "url": "https://www.nosdeputes.fr/jerome-guedj"},
                ],
                "score": None,
            },
            {
                "value": "faure_vallaud",
                "group": "PS",
                "label": "Olivier Faure / Boris Vallaud — PS (courant majoritaire)",
                "note": "Faure is PS first secretary; Vallaud leads the PS parliamentary group. Social-democrat, pro-Ukraine, architects of NFP coalition in 2024.",
                "refs": [
                    {"label": "Assemblée nationale — Groupe Socialistes et apparentés", "url": "https://www.assemblee-nationale.fr/dyn/17/organes/groupes/socialistes-et-apparentes"},
                ],
                "score": None,
            },
            {
                "value": "hollande",
                "group": "PS",
                "label": "François Hollande — PS (aile sociale-libérale)",
                "note": "President 2012–2017. Implemented the Pacte de responsabilité (2014): €40bn in employer tax relief, described by critics as social-liberal austerity. Pro-Atlantic.",
                "refs": [
                    {"label": "Wikipedia — Pacte de responsabilité et de solidarité", "url": "https://fr.wikipedia.org/wiki/Pacte_de_responsabilit%C3%A9_et_de_solidarit%C3%A9"},
                    {"label": "Politis — Hollande et le 'blairisme droitisé'", "url": "https://www.politis.fr/articles/2014/08/hollande-met-en-pratique-une-version-droitisee-du-blairisme-28034/"},
                ],
                "score": None,
            },
            # ── Écologistes ──────────────────────────────────────────────────
            {
                "value": "tondelier",
                "group": "Écologistes",
                "label": "Marine Tondelier — Les Écologistes",
                "note": "Elected national secretary of Les Écologistes in December 2022 (90.8% of vote). Green New Deal platform, feminist, pro-European. Running in the 2027 left primary.",
                "refs": [
                    {"label": "Wikipedia — Marine Tondelier (élection secrétaire nationale)", "url": "https://en.wikipedia.org/wiki/Marine_Tondelier"},
                    {"label": "Reporterre — Tondelier candidate à la primaire de la gauche 2027", "url": "https://reporterre.net/Presidentielle-2027-Marine-Tondelier-candidate-a-une-primaire-de-la-gauche"},
                ],
                "score": None,
            },
            {
                "value": "batho",
                "group": "Écologistes",
                "label": "Delphine Batho — Génération Écologie",
                "note": "Resigned from the Ayrault government on 2 July 2013 after publicly calling the ecology budget 'bad'. Called for a moratorium on 5G in July 2020.",
                "refs": [
                    {"label": "Légifrance — Décret du 2 juillet 2013 mettant fin aux fonctions de Batho", "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000027650341"},
                    {"label": "Batho réclame un moratoire sur la 5G (juillet 2020)", "url": "https://www.jeanmarcmorandini.com/article-430063-delphine-batho-deputee-eds-ecologie-democratie-solidarite-reclame-un-moratoire-sur-la-5g-s-interrogeant-sur-l-utilite-et-l-impact-environnemental-de-cette-technologie.html"},
                ],
                "score": None,
            },
            {
                "value": "s_rousseau",
                "group": "Écologistes",
                "label": "Sandrine Rousseau — EELV (aile radicale)",
                "note": "AN deputy for Paris (9th constituency) since 2022. Advocates degrowth, intersectional eco-feminism. Most radical of the three ecologist candidates.",
                "refs": [
                    {"label": "Assemblée nationale — Fiche Sandrine Rousseau (Paris, EELV)", "url": "https://www.assemblee-nationale.fr/dyn/deputes/PA795076"},
                    {"label": "France 3 — Portrait: 'l'écoféministe Sandrine Rousseau entre à l'AN'", "url": "https://france3-regions.franceinfo.fr/paris-ile-de-france/paris/portrait-legislatives-2022-l-ecofeministe-sandrine-rousseau-entre-a-l-assemblee-nationale-2566456.html"},
                ],
                "score": None,
            },
            # ── Centre-gauche ─────────────────────────────────────────────────
            {
                "value": "glucksmann",
                "group": "Centre-gauche",
                "label": "Raphaël Glucksmann — Place Publique / PS",
                "note": "Led the S&D-affiliated list to 13.83% in the 2024 European elections. His signature issue: anti-Putin engagement, Ukraine solidarity, documented Russian war crimes.",
                "refs": [
                    {"label": "Franceinfo — Résultats liste Glucksmann, européennes 2024", "url": "https://www.franceinfo.fr/elections/resultats-des-europeennes-2024-la-liste-de-raphael-glucksmann-obtient-14-des-voix-selon-notre-estimation-ipsos_6576611.html"},
                    {"label": "Glucksmann — Newsletter depuis l'Ukraine, fév. 2025", "url": "https://raphaelglucksmann.kessel.media/posts/pst_bde552542ce94673b5d60ad3fd1e33c3/je-vous-ecris-dukraine-la-ou-se-joue-lavenir-de-leurope"},
                ],
                "score": None,
            },
            {
                "value": "cazeneuve",
                "group": "Centre-gauche",
                "label": "Bernard Cazeneuve — La Convention",
                "note": "Prime Minister December 2016–May 2017. Interior Minister 2014–2017 (oversaw state of emergency post-2015 attacks). Founded La Convention in March 2023 as a conservative PS counter to LFI.",
                "refs": [
                    {"label": "L'Hémicycle — Cazeneuve lance La Convention (mars 2023)", "url": "https://lhemicycle.com/2023/03/09/bernard-cazeneuve-lance-la-convention/"},
                    {"label": "France Archives — Cabinet Cazeneuve, Premier ministre", "url": "https://francearchives.gouv.fr/fr/authorityrecord/FRAN_NP_051540"},
                ],
                "score": None,
            },
            # ── Centre ───────────────────────────────────────────────────────
            {
                "value": "bayrou",
                "group": "Centre",
                "label": "François Bayrou — MoDem / Premier ministre (en exercice)",
                "note": "Appointed PM by Macron on 9 January 2025. Three-time presidential candidate (2002, 2007, 2012). Independent centrist tradition; Gaullist vision of the state.",
                "refs": [
                    {"label": "Légifrance — Arrêté du 9 janv. 2025 composition gouvernement Bayrou", "url": "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050963054"},
                    {"label": "CNews — Bayrou, candidat en 2002, 2007, 2012, n'envisage pas 2027", "url": "https://www.cnews.fr/france/2026-04-01/presidentielle-2027-candidat-en-2002-2007-et-2012-francois-bayrou-nenvisage-pas"},
                ],
                "score": None,
            },
            {
                "value": "e_philippe",
                "group": "Centre",
                "label": "Édouard Philippe — Horizons",
                "note": "Prime Minister 2017–2020. Founded Horizons in 2021. Leading presidential polls in 2025–2026 surveys. Pro-business, pro-Atlantic.",
                "refs": [
                    {"label": "Public Sénat — Philippe favori pour 2027 selon les sondages", "url": "https://www.publicsenat.fr/actualites/politique/sondage-edouard-philippe-bondit-lex-premier-ministre-desormais-favori-pour-2027"},
                    {"label": "Euronews — Philippe donné vainqueur par deux sondages (mars 2026)", "url": "https://fr.euronews.com/2026/03/31/presidentielle-francaise-edouard-philippe-donne-vainqueur-par-deux-sondages-face-a-jordan-bardella"},
                ],
                "score": None,
            },
            {
                "value": "attal",
                "group": "Centre",
                "label": "Gabriel Attal — Renaissance",
                "note": "Youngest PM in French history (born 1989), appointed 9 January 2024, resigned 16 July 2024. Right-leaning Macronist; signature issues: school authority, security.",
                "refs": [
                    {"label": "Public Sénat — Attal, 'plus jeune Premier ministre de la Ve République'", "url": "https://www.publicsenat.fr/actualites/politique/nomme-a-matignon-gabriel-attal-devient-le-plus-jeune-premier-ministre-de-la-ve-republique"},
                ],
                "score": None,
            },
            {
                "value": "darmanin",
                "group": "Centre",
                "label": "Gérald Darmanin — Renaissance",
                "note": "Interior Minister 2020–2024. Led the controversial immigration and asylum bill signed in January 2024 ('loi Darmanin'). Hardline security and immigration restrictionist.",
                "refs": [
                    {"label": "GISTI — Documentation complète de la loi Darmanin immigration 2024", "url": "https://www.gisti.org/spip.php?article6862"},
                    {"label": "Sénat — Dossier législatif projet de loi immigration", "url": "https://www.senat.fr/dossier-legislatif/pjl22-304.html"},
                ],
                "score": None,
            },
            {
                "value": "de_villepin",
                "group": "Centre",
                "label": "Dominique de Villepin — France Humaniste",
                "note": "Gaullist. As Foreign Minister, gave the famous speech at the UN Security Council on 14 February 2003 opposing the Iraq invasion. Favours diplomacy and sovereignty over NATO integration.",
                "refs": [
                    {"label": "Wikipedia — Discours de Villepin à l'ONU, 14 fév. 2003", "url": "https://fr.wikipedia.org/wiki/Discours_de_Dominique_de_Villepin_aux_Nations_unies"},
                    {"label": "INA — 14 février 2003 : de Villepin, Irak, ONU (archive)", "url": "https://www.ina.fr/ina-eclaire-actu/14-fevrier-2003-france-etats-unis-de-villepin-irak-guerre-onu"},
                ],
                "score": None,
            },
            # ── Droite ───────────────────────────────────────────────────────
            {
                "value": "retailleau",
                "group": "Droite",
                "label": "Bruno Retailleau — LR / Ministre de l'Intérieur",
                "note": "LR senator, appointed Interior Minister on 21 September 2024 under Barnier. Socially conservative Catholic; hardline on immigration, security, and public order.",
                "refs": [
                    {"label": "Gendarmerie nationale — Retailleau nommé ministre de l'Intérieur, 21 sept. 2024", "url": "https://www.gendarmerie.interieur.gouv.fr/gendinfo/actualites/2024/bruno-retailleau-nomme-ministre-de-l-interieur"},
                    {"label": "Parlons-politique — Son catholicisme revendiqué", "url": "https://www.parlons-politique.fr/analyses-opinions/bruno-retailleau-le-cardinal-nathalie-schuck-biographie-du-president-lr-son-catholicisme-revendique-et-sa-longue-quete-du-pouvoir_3842/"},
                ],
                "score": None,
            },
            {
                "value": "bertrand",
                "group": "Droite",
                "label": "Xavier Bertrand — La France ensemble",
                "note": "President of the Hauts-de-France region. Repeatedly refused any electoral alliance with the RN — has called for exclusion of LR candidates who approach Le Pen.",
                "refs": [
                    {"label": "LCP — Bertrand souhaite l'exclusion des candidats LR proches du RN", "url": "https://lcp.fr/actualites/dehors-xavier-bertrand-souhaite-l-exclusion-des-candidats-lr-qui-se-rapprochent-de-l"},
                    {"label": "France 3 — Portrait Bertrand, président Hauts-de-France", "url": "https://france3-regions.franceinfo.fr/hauts-de-france/nord-0/lille/entretien-xavier-bertrand-president-de-la-region-hauts-de-france-quand-on-veut-vraiment-ameliorer-la-vie-des-gens-c-est-au-sommet-de-l-etat-qu-on-peut-le-faire-3253309.html"},
                ],
                "score": None,
            },
            {
                "value": "lisnard",
                "group": "Droite",
                "label": "David Lisnard — Nouvelle Énergie (fondée 2021)",
                "note": "Mayor of Cannes. Left LR in March 2026 after accusing the party of a rigged vote. Economic libertarian: pro-decentralisation, lower taxes, free market.",
                "refs": [
                    {"label": "LCP — Lisnard quitte LR et dénonce un 'vote truqué' (mars 2026)", "url": "https://lcp.fr/actualites/david-lisnard-quitte-lr-et-denonce-un-vote-truque-au-sein-du-parti-pour-la"},
                    {"label": "Public Sénat — Lisnard annonce sa candidature 2027", "url": "https://www.publicsenat.fr/actualites/politique/presidentielle-2027-david-lisnard-maire-de-cannes-annonce-sa-candidature-et-quitte-officiellement-les-lr"},
                ],
                "score": None,
            },
            {
                "value": "dupont_aignan",
                "group": "Droite",
                "label": "Nicolas Dupont-Aignan — Debout la France",
                "note": "Souverainiste right, anti-EU, voted against France–Ukraine security agreements in the AN. Gaullist tradition without the Gaullist mainstream.",
                "refs": [
                    {"label": "Assemblée nationale — Fiche Nicolas Dupont-Aignan", "url": "https://www.assemblee-nationale.fr/dyn/deputes/PA1206"},
                    {"label": "Public Sénat — Dupont-Aignan contre le soutien à l'Ukraine", "url": "https://www.publicsenat.fr/actualites/politique/soutien-a-lukraine-on-entraine-la-france-dans-un-engrenage-terrible-juge-nicolas-dupont-aignan"},
                ],
                "score": None,
            },
            # ── Extrême droite ────────────────────────────────────────────────
            {
                "value": "le_pen",
                "group": "Extrême droite",
                "label": "Marine Le Pen / Jordan Bardella — Rassemblement National",
                "note": "Le Pen condemned on 31 March 2025 by the Paris correctional court (4 years prison, 5 years ineligibility with immediate execution) for misappropriation of EU Parliament funds. Appeal proceedings January–February 2026; decision pending. Bardella is backup candidate.",
                "refs": [
                    {"label": "LCP — Le Pen condamnée à 5 ans d'inéligibilité (31 mars 2025)", "url": "https://lcp.fr/actualites/justice-marine-le-pen-condamnee-a-cinq-ans-d-ineligibilite-avec-execution-immediate-pour"},
                    {"label": "Euronews — Le Pen et 8 eurodéputés RN reconnus coupables", "url": "https://fr.euronews.com/my-europe/2025/03/31/marine-le-pen-et-huit-eurodeputes-du-rn-reconnus-coupables-de-detournement-de-fonds-public"},
                    {"label": "Touteleurope — L'affaire des assistants du RN au Parlement européen", "url": "https://www.touteleurope.eu/institutions/qu-est-ce-que-l-affaire-des-assistants-du-rn-au-parlement-europeen/"},
                ],
                "score": None,
            },
            {
                "value": "zemmour",
                "group": "Extrême droite",
                "label": "Éric Zemmour — Reconquête",
                "note": "'Remigration' is his signature policy (mass expulsion of immigrants). Definitively convicted for incitement to hatred (statements on unaccompanied minors, 2020) by Court of Cassation in December 2025.",
                "refs": [
                    {"label": "Public Sénat — Zemmour 'assume' le terme remigration", "url": "https://www.publicsenat.fr/actualites/non-classe/presidentielle-2022-eric-zemmour-detaille-son-programme-et-assume-le-terme"},
                    {"label": "Europe 1 — Zemmour veut un 'ministère de la remigration'", "url": "https://www.europe1.fr/politique/presidnetielle-eric-zemmour-veut-creer-un-ministere-de-la-remigration-4101123"},
                ],
                "score": None,
            },
            {
                "value": "philippot",
                "group": "Extrême droite",
                "label": "Florian Philippot — Les Patriotes",
                "note": "Ex-RN vice-president. Led anti-vaccine and anti-lockdown movements 2020–2022. Frames the Ukraine war as US/NATO aggression — called Ukrainians 'Nazis' in March 2022.",
                "refs": [
                    {"label": "CNews — Philippot qualifie les Ukrainiens de 'nazis', mars 2022", "url": "https://www.cnews.fr/france/2022-03-07/guerre-en-ukraine-philippot-qualifie-les-ukrainiens-de-nazis-1189981"},
                    {"label": "StreetPress — Philippot dans le milieu antivax/complotiste", "url": "https://www.streetpress.com/sujet/1714405192-philippot-pays-conspirationnistes-complotistes-palomba-extreme-droite-elections-europeennes-covid-antivax"},
                ],
                "score": None,
            },
            {
                "value": "asselineau",
                "group": "Extrême droite",
                "label": "François Asselineau — Union Populaire Républicaine (UPR)",
                "note": "Founded UPR in March 2007 with Frexit as its sole platform. Opposed all COVID measures (vaccines, health pass) and advocated Ivermectin in 2021.",
                "refs": [
                    {"label": "Wikipedia FR — UPR fondée le 25 mars 2007 par Asselineau", "url": "https://fr.wikipedia.org/wiki/Union_populaire_r%C3%A9publicaine_(2007)"},
                    {"label": "Wikipedia EN — Asselineau (COVID positions)", "url": "https://en.wikipedia.org/wiki/Fran%C3%A7ois_Asselineau"},
                    {"label": "Public Sénat — UPR campagne pour le Frexit", "url": "https://www.publicsenat.fr/actualites/non-classe/europeennes-asselineau-upr-lance-sa-campagne-en-faveur-d-un-frexit-134828"},
                ],
                "score": None,
            },
            # ── Non-vote ─────────────────────────────────────────────────────
            {
                "value": "none",
                "group": "Non-vote",
                "label": "No vote — I abstain / spoil my ballot / don't participate in elections",
                "note": None,
                "refs": [],
                "score": None,
            },
        ],
    },
]

# Expected political profiles (eco, econ, ukraine, police) on 1-4 scale
POLITICAL_PROFILES = [
    {
        "name": "Radical Left",
        "label": "Radical Left",
        "description": (
            "You stand to the LEFT of LFI on ecology and reject electoral politics as a primary strategy. "
            "Core convictions: degrowth is non-negotiable, direct action is legitimate, and ecology without "
            "feminism and class struggle is 'just gardening'. "
            "Closest to: Soulèvements de la Terre (Basile Dutertre, Benoît Feuillu), "
            "NPA / Révolution Permanente (Olivier Besancenot, Philippe Poutou), "
            "Extinction Rebellion France, Les Amis de la Terre, ATTAC, Scientifiques en Rébellion, "
            "and the radical wing of EELV (Sandrine Rousseau). "
            "Unlike LFI, this current prioritizes movement-building over parliament."
        ),
        "color": "#1b5e20",
        "expected_parties": ["radical_left", "lfi", "none"],
        "vector": {"eco": 4.0, "econ": 4.0, "ukraine": 2.5, "police": 4.0},
    },
    {
        "name": "Abstentionniste",
        "label": "Abstentionniste / Non-voter",
        "description": (
            "Your positions don't map neatly onto any French political party — or you've lost faith "
            "in the electoral system entirely. "
            "In 2024, 33% of registered voters abstained in the first round of legislatives; "
            "abstention is structurally highest among young people, working-class voters, and "
            "those who feel unrepresented by the party system. "
            "Abstention is a political act: it can signal disillusionment, tactical refusal, "
            "or active rejection of the available options."
        ),
        "color": "#546e7a",
        "expected_parties": ["none"],
        "vector": {"eco": 2.5, "econ": 2.5, "ukraine": 2.5, "police": 2.5},
    },
    {
        "name": "La France Insoumise / NFP",
        "label": "La France Insoumise (NFP)",
        "description": "Anti-capitalist, pro-redistribution, skeptical of NATO expansion, strongly anti-police violence. You likely voted NFP in 2024.",
        "color": "#c62828",
        "expected_parties": ["lfi", "radical_left"],
        "vector": {"eco": 3.0, "econ": 4.0, "ukraine": 2.0, "police": 4.0},
    },
    {
        "name": "Écologiste",
        "label": "Écologiste (EELV / Les Verts)",
        "description": "Ecology first, feminist, pro-European, moderate on redistribution. You likely voted EELV or Glucksmann in 2024.",
        "color": "#388e3c",
        "expected_parties": ["ecologists", "pcf_ps"],
        "vector": {"eco": 4.0, "econ": 3.0, "ukraine": 3.5, "police": 3.5},
    },
    {
        "name": "Social Democrat",
        "label": "Social Democrat (PS / Place Publique)",
        "description": "Progressive on social issues, pro-European, moderate ecologist. Favors regulation over revolution. Closest to PS or Glucksmann's Place Publique.",
        "color": "#e53935",
        "expected_parties": ["pcf_ps", "centre_left", "ecologists"],
        "vector": {"eco": 3.0, "econ": 3.0, "ukraine": 3.5, "police": 3.0},
    },
    {
        "name": "Liberal Centrist",
        "label": "Liberal Centrist (Renaissance / Macroniste)",
        "description": "Pro-market with social guardrails, strongly pro-European and pro-Ukraine, technocratic approach to ecology. You likely voted Macron in 2022.",
        "color": "#fbc02d",
        "expected_parties": ["centre", "centre_left"],
        "vector": {"eco": 2.0, "econ": 2.0, "ukraine": 3.5, "police": 2.0},
    },
    {
        "name": "Conservative Right",
        "label": "Conservative Right (LR / Gaulliste)",
        "description": "Pro-security, skeptical of redistribution, pro-Atlantic alliance, law-and-order on police. Classic Gaullist or LR voter.",
        "color": "#1565c0",
        "expected_parties": ["right", "centre"],
        "vector": {"eco": 2.0, "econ": 1.5, "ukraine": 3.0, "police": 1.5},
    },
    {
        "name": "National Populist",
        "label": "National Populist (RN)",
        "description": "Souverainiste, skeptical of EU and NATO, anti-immigration framing of social issues, strong law-and-order. Closest to Marine Le Pen's RN.",
        "color": "#6a1b9a",
        "expected_parties": ["rn"],
        "vector": {"eco": 1.5, "econ": 2.0, "ukraine": 1.5, "police": 1.0},
    },
    {
        "name": "Hard Right",
        "label": "Hard Right (Reconquête / Identitaire)",
        "description": "Anti-immigration identity politics, minimal state intervention economically, maximum authority for police, hostility to environmental regulation. Closest to Zemmour (Reconquête), Philippot (Les Patriotes), Asselineau (UPR).",
        "color": "#4a148c",
        "expected_parties": ["far_right"],
        "vector": {"eco": 1.0, "econ": 1.0, "ukraine": 2.0, "police": 1.0},
    },
]

# Contradiction pairs for troll/consistency detection
# (q1_id, q1_value, q2_id, q2_value, severity, explanation)
CONTRADICTION_PAIRS = [
    # Within environment
    ("eco_activism", "vanguard", "eco_economy", "growth",
     "major", "Supporting radical eco-activists while believing in unlimited GDP growth is internally contradictory."),
    ("eco_activism", "terrorist", "eco_economy", "degrowth",
     "major", "Calling eco-activists terrorists while supporting degrowth is contradictory."),
    # Within social
    ("wealth_tax", "trickle_down", "intersectionality", "intersectional",
     "moderate", "Trickle-down economics is structurally incompatible with an intersectional class-struggle worldview."),
    ("wealth_tax", "zucman_plus", "intersectionality", "traditional",
     "major", "Aggressive wealth redistribution and traditional conservative values rarely coexist."),
    # Within Ukraine
    ("ukraine_support", "troops", "ukraine_origins", "russia_defending",
     "major", "Supporting sending troops to Ukraine while believing Russia is the victim is a direct contradiction."),
    ("ukraine_support", "troops", "ukraine_origins", "nato_proxy",
     "major", "Supporting sending French troops while framing the conflict as a NATO proxy war is incoherent."),
    ("ukraine_support", "no_support", "ukraine_origins", "illegal_invasion",
     "major", "Recognizing Russia's illegal invasion but wanting to stop all support is a significant inconsistency."),
    # Within police
    ("systemic_racism", "denial", "lbd_armament", "ban_now",
     "major", "Denying police violence while wanting to ban LBDs for causing severe injuries is contradictory."),
    ("systemic_racism", "systemic", "lbd_armament", "more_force",
     "major", "Recognizing systemic racism while calling for even more police firepower is contradictory."),
    # Cross-section
    ("wealth_tax", "trickle_down", "state_role", "planification",
     "major", "Trickle-down economics is fundamentally incompatible with state economic planning."),
    ("wealth_tax", "zucman_plus", "state_role", "sovereign_state",
     "moderate", "Radical wealth redistribution combined with exclusionary nationalist state is a RN-style contradiction."),
    ("eco_economy", "degrowth", "eco_activism", "terrorist",
     "moderate", "Supporting degrowth but opposing the movements pushing hardest for it is inconsistent."),
    ("systemic_racism", "denial", "intersectionality", "intersectional",
     "moderate", "Denying systemic racism while embracing intersectionality (which centers racial justice) is contradictory."),
]

# Per-candidate expected dimension ranges for Q10 calibration (eco, econ, ukraine, police) 1–4 scale
PARTY_EXPECTED = {
    # ── Extrême gauche ──────────────────────────────────────────────────────
    "arthaud":       {"eco": (3.0, 4.0), "econ": (3.5, 4.0), "ukraine": (1.0, 2.5), "police": (3.5, 4.0)},
    "autain":        {"eco": (3.0, 4.0), "econ": (3.5, 4.0), "ukraine": (2.0, 3.5), "police": (3.5, 4.0)},
    "poutou":        {"eco": (3.0, 4.0), "econ": (3.5, 4.0), "ukraine": (1.0, 2.5), "police": (3.5, 4.0)},
    # ── LFI ─────────────────────────────────────────────────────────────────
    "melenchon":     {"eco": (2.5, 4.0), "econ": (3.5, 4.0), "ukraine": (1.0, 2.5), "police": (3.0, 4.0)},
    "ruffin":        {"eco": (2.5, 3.5), "econ": (3.0, 4.0), "ukraine": (2.0, 3.0), "police": (3.0, 4.0)},
    # ── PCF ─────────────────────────────────────────────────────────────────
    "roussel":       {"eco": (2.0, 3.5), "econ": (3.5, 4.0), "ukraine": (2.0, 3.0), "police": (2.0, 3.0)},
    "brossat":       {"eco": (2.5, 3.5), "econ": (3.5, 4.0), "ukraine": (2.0, 3.0), "police": (3.0, 4.0)},
    # ── PS ──────────────────────────────────────────────────────────────────
    "guedj":         {"eco": (2.5, 3.5), "econ": (3.0, 4.0), "ukraine": (3.0, 4.0), "police": (2.5, 3.5)},
    "faure_vallaud": {"eco": (2.0, 3.0), "econ": (2.5, 3.5), "ukraine": (3.0, 4.0), "police": (2.0, 3.0)},
    "hollande":      {"eco": (2.0, 3.0), "econ": (2.0, 3.0), "ukraine": (3.0, 4.0), "police": (1.5, 2.5)},
    # ── Écologistes ─────────────────────────────────────────────────────────
    "tondelier":     {"eco": (3.5, 4.0), "econ": (2.5, 3.5), "ukraine": (3.0, 4.0), "police": (3.0, 4.0)},
    "batho":         {"eco": (3.5, 4.0), "econ": (3.0, 4.0), "ukraine": (2.5, 3.5), "police": (3.0, 4.0)},
    "s_rousseau":    {"eco": (3.5, 4.0), "econ": (3.5, 4.0), "ukraine": (2.5, 3.5), "police": (3.5, 4.0)},
    # ── Centre-gauche ───────────────────────────────────────────────────────
    "glucksmann":    {"eco": (2.5, 3.5), "econ": (2.5, 3.0), "ukraine": (3.5, 4.0), "police": (2.0, 3.0)},
    "cazeneuve":     {"eco": (1.5, 2.5), "econ": (2.0, 3.0), "ukraine": (3.0, 4.0), "police": (1.5, 2.5)},
    # ── Centre ──────────────────────────────────────────────────────────────
    "bayrou":        {"eco": (1.5, 2.5), "econ": (1.5, 2.5), "ukraine": (3.0, 4.0), "police": (1.5, 2.5)},
    "e_philippe":    {"eco": (1.5, 2.5), "econ": (1.5, 2.5), "ukraine": (3.0, 4.0), "police": (1.5, 2.5)},
    "attal":         {"eco": (1.5, 2.5), "econ": (1.5, 2.5), "ukraine": (3.0, 4.0), "police": (1.0, 2.0)},
    "darmanin":      {"eco": (1.5, 2.5), "econ": (1.5, 2.5), "ukraine": (2.5, 3.5), "police": (1.0, 1.5)},
    "de_villepin":   {"eco": (1.5, 2.5), "econ": (1.5, 2.5), "ukraine": (1.5, 2.5), "police": (1.5, 2.5)},
    # ── Droite ──────────────────────────────────────────────────────────────
    "retailleau":    {"eco": (1.0, 2.0), "econ": (1.0, 2.0), "ukraine": (2.5, 4.0), "police": (1.0, 1.5)},
    "bertrand":      {"eco": (1.5, 2.5), "econ": (1.5, 2.0), "ukraine": (2.5, 4.0), "police": (1.0, 2.0)},
    "lisnard":       {"eco": (1.0, 2.0), "econ": (1.0, 1.5), "ukraine": (2.5, 4.0), "police": (1.0, 2.0)},
    "dupont_aignan": {"eco": (1.0, 2.0), "econ": (1.5, 2.5), "ukraine": (1.0, 2.0), "police": (1.0, 1.5)},
    # ── Extrême droite ──────────────────────────────────────────────────────
    "le_pen":        {"eco": (1.0, 2.0), "econ": (1.0, 2.5), "ukraine": (1.0, 2.0), "police": (1.0, 1.5)},
    "zemmour":       {"eco": (1.0, 1.5), "econ": (1.0, 2.0), "ukraine": (1.5, 2.5), "police": (1.0, 1.0)},
    "philippot":     {"eco": (1.0, 2.0), "econ": (1.5, 2.5), "ukraine": (1.0, 1.5), "police": (1.0, 1.5)},
    "asselineau":    {"eco": (1.0, 2.0), "econ": (1.0, 2.0), "ukraine": (1.0, 1.5), "police": (1.0, 1.5)},
    # ── Non-vote ────────────────────────────────────────────────────────────
    "none":          None,
}
