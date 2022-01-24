# Annotation Protocol

This directory contains the annotation protocol that will be used. It is called the
"Protocol for Orthographic Transcription". The protocol is written in both English
and Dutch.
- English Version: [protocol_en.pdf](protocol_en.pdf)
- Dutch Version: [protocol_nl.pdf](protocol_nl.pdf)


The protocol is detailed, and to make easier for the later NLP analysis, we will not
include all of the rules. The selected rules are listed in the section below.

## 1. Annotation Rules

**Here is the list of annotation rules that must be followed.**

You may also want to browse through section D for spelling convention! \
But note that the tags \*d, \*z, \*n and \*t are not used in our annotation rules.


**B1. Use the new spelling.**
- Apply the new rules also to the placing of hyphens (e.g. "zee-engte"), the inserted
"n" (e.g. "pannenkoek"), etc.

**B2. Mark sections that are difficult to understand with "xxx" or "Xxx".**
- C9. Use xxx, -xxx, xxx- or -xxx- for incomprehensible utterances.
- C10. Use Xxx with incomprehensible personal names or titles.

**B3. Do NOT use a capital letter at the beginning of a sentence. DO use capital
letters for proper names (e.g. "Bert Jansens") and for titles of books, records, etc.
(e.g. "De Naam Van De Roos").**

**B4. Use the codes \*v, \*a, \*u, \*x where necessary or logical.**
- Never use more than one of the above codes per word. Choose the most suitable code.
1. **use \*v for foreign words**
   - *e.g. "see\*v you\*v tomorrow\*v"*
2. **use \*a for words cut short or interrupted** 
   - *e.g. "uitges\*a", "verpr\*a"*
   - C6a. Where only one sound is spoken:
     - *e.g. "m\*a ik weet het niet"*
   - C6b. Where a word is repeated in its entirety, use neither a code nor a hyphen.
     - *e.g. "ik ik ik weet het niet"*
3. **use \*u to show onomatopoeia and slips of the tongue**
   - *e.g. "boink\*u", "gespreken\*u"*
   - C7a. onomatopoeia and (deliberate) distortion:
     - *e.g. "boink\*u hoorde ik"*
     - *e.g. "hij zegt voor de grap toekenbas\*u in plaats van boekentas"*
   - C7b. slips of the tongue:
     - *e.g. "ik heb me verspraakt\*u"*
     - *e.g. "KPN annuleert fusie met Spaans bedrijf alduns\*u aldus een kop in de krant"*
   - C7c. all cases of slips of the tongue and resumptions WITHIN A WORD. In contrast
     with the \*a tag, the word is completed!: 
     - *e.g. "hij is nog niet naar de kapper gewee-weest\*u"*
     - *e.g. "ze heeft haar ring ver-uh-uh-patst\*u"*
4. **use \*x for words where you are not sure if you have understood them correctly**
   - C8a. *e.g. "hij kan dertig\*x bladzijden per uur uit het hoofd leren"*
   - C8b. *e.g. "ze zei dat Jan-Peter\*x nog zou komen"*

**B6. Only use the punctuation marks full stop, question mark, and ellipsis. No other
punctuation marks are used!**
- E1. Use a full stop "." at the end of an utterance. Avoid making unnecessarily long
  sentences: if you *could* intuitively place a full stop, then do so.
- E2. Use a question mark "?" to indicate a question.
- E3. Use ellipsis "..." when a sentence, for whatever reason, is not finished.
  - *e.g. "ik ben niet goed... ik ben niet goed wakker"* \
    ⟶ "ik ben niet goed wakker" **CAN** stand on its own
  - *e.g. "ik ben niet goed uit\*a... ik ben niet goed wakker"* \
    ⟶ "ik ben niet goed wakker" **CAN** stand on its own
    
  But do NOT use it when the second part cannot stand on its own, i.e. is not a full
  sentence.
  - *e.g. "ik ben niet goed uit\*a niet goed wakker"* \
    ⟶ "niet goed wakker" **CANNOT** stand on its own
  - *e.g. "ik ben niet goed niet goed wakker"* \
    ⟶ "niet goed wakker" **CANNOT** stand on its own

**B7. Use "ggg" for clearly audible speaker’s sounds.**
- C11a. *e.g. "even mijn keel schrapen hoor. ggg. zo dat is beter"*
- C11b. *e.g. "ken je die mop van die man die naar Parijs ging? nou hij ging niet.
  ggg."* \
  ⟶ laughter marked with "ggg"
- C11c. *e.g. "ggg. gezondheid"* \
  ⟶ sneeze marked with "ggg"
