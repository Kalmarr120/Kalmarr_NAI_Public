# Format and Customization Research

<details>
<summary> Contents </summary>

### Table of Contents

- [Format and Customization Research](#format-and-customization-research)
    - [Table of Contents](#table-of-contents)
  - [1. Lorebook Settings](#1-lorebook-settings)
    - [1.1 Scaffolds and Recommended Settings](#11-scaffolds-and-recommended-settings)
      - [1.1(a) OPVAM Scaffold](#11a-opvam-scaffold)
      - [1.1(b)](#11b)
  - [2. Lorebook Application (AKA Formatting)](#2-lorebook-application-aka-formatting)
    - [2.1 Featherlite](#21-featherlite)
      - [2.1(a) Featherlite Testing Note](#21a-featherlite-testing-note)
      - [2.1(b) Featherlite Example Entries](#21b-featherlite-example-entries)
      - [2.1(c) Featherlite Conversion from AID (with examples)](#21c-featherlite-conversion-from-aid-with-examples)
    - [2.2 Monky's Caveman](#22-monkys-caveman)
    - [2.3 Current Format Testing To-Do](#23-current-format-testing-to-do)
      - [2.3(a) JSON/Python-like](#23a-jsonpython-like)
      - [2.3(b) `[ ]` Prose Format](#23b---prose-format)
      - [2.3(c) Regular Prose Format](#23c-regular-prose-format)
  - [3. Story Settings](#3-story-settings)
    - [3.1 Generation Settings](#31-generation-settings)
    - [3.2 Token Banning](#32-token-banning)
  - [4. Author's Notes](#4-authors-notes)
    - [4.1 Authors](#41-authors)
    - [4.2 Writing Styles](#42-writing-styles)
      - [4.2(a) Other Writing Style Application Methods](#42a-other-writing-style-application-methods)
    - [4.3 Genres, Themes, Etc.](#43-genres-themes-etc)
  - [5. Person Perspective](#5-person-perspective)
  - [6. Signposts](#6-signposts)
    - [6.1 `***` Signposts](#61--signposts)
    - [6.2 `***` In-Entry Signpost](#62--in-entry-signpost)
    - [6.3 `<<•>>>` Signpost](#63--signpost)
    - [6.4 Other Signposts](#64-other-signposts)
      - [6.4(a) `* * *` Signpost](#64a----signpost)
      - [6.4(b) `⁂` Signpost](#64b--signpost)
  - [7. Other Testing](#7-other-testing)
    - [7.1 "Director" Entries](#71-director-entries)
    - [7.2 Scene Separators](#72-scene-separators)
      - [7.2(a) Asterix Separator](#72a-asterix-separator)
      - [7.2(b) `<|endoftext|>` Separator](#72b-endoftext-separator)
    - [7.3 Input Tools](#73-input-tools)
    - [7.4 Prompt Generation](#74-prompt-generation)
  - [8. Character/Species "Generator"](#8-characterspecies-generator)
  - [9. Glossary](#9-glossary)
  - [10. Appendix](#10-appendix)
    - [11. Testing Methods (TBC)](#11-testing-methods-tbc)

</details>
<br>

Welcome to my Novel AI (NAI) primary research, testing, and information document.

As an introduction, this document contains an array of information relating to settings, lorebook structuring, and other key parts of manipulating NAI into generating outputs that are rational, consistent, accurate, and enjoyable. This information comes from a variety of sources—people from the former #world-info community in AI Dungeon (AID), researchers in the NAI #community-research channel, and others. I will attribute ideas where possible. Please reach out to me on Discord (Kalmarr) if you believe anything is mis-attributed.

Recommendations in this document may not work for everyone, but they should at least give you an insight into where you can use NAI’s capabilities to suit your usage. I encourage you to test things even if they did not work for me. They could be useful for how you use the service.

As a user of the service, my goal is to provide a foundational structure of information guiding the AI into writing a story using my ideas and with as minimal guidance as possible. My goal is _not_ to have the AI write in my particular style, or to have it flesh out stories I write myself. If you are in the latter category, please keep that in mind as you use recommendations presented in this document. As a former user of EWIJSON (a powerful script) in AID, my preference colours much of my perspective here, encouraging me to take a heavy hand with the AI. Some users may prefer to take a lighter approach. My use of non-human characters in my stories also colours my preferences. I expect simpler use cases with fewer unusual characters/attributes will presumably behave well without brute force, particularly in Sigurd v3.

The information will reflect the current highest Opus tier model (_now Sigurd v3_) unless otherwise stated.

Please note that I will not describe my testing in granular detail, e.g. always including rates of success/failure or numbers of generations. At this stage, I am testing using dozens of outputs in comparable situations to determine whether output appears to be improved. For example, how often I see the need to retry an output is a helpful metric. I will try to describe results in relative terms (clearer, more accurate, more creative, etc.) when compared to other settings/entries.

Happy writing!

~Kalmarr

---

## 1. Lorebook Settings

Please jump to [section 1.1](#11-scaffolds-and-recommended-settings) for recommended settings if you wish to skip the explainer.

The Lorebook is the system that you will primarily use to tell the AI what you want it to remember and focus on as it writes. It provides guidance that assists the AI with remembering character traits, locations, concepts, and many other things. In NAI, the Lorebook has incredibly helpful settings that allow users to give very specific instructions to where in the context an entry should be "injected" (i.e. added behind the scenes). Generally, the closer to the context, the easier it is for the AI to remember and pull from.

The most useful settings in the Lorebook (under _show advanced settings_) are:

- `Insertion Order:` formerly called Priority, `Order` refers to, essentially, the order in which types of context are built in the overall context. The lower the number as an integer (`-700` as an example), the closer to input the order type is injected into the context. The number is, in essence, completely arbitrary and used as the basis of entries' relative position to each other. There is a current trend towards changing all numbers to positive ones, likely for ease of use.
- `Insertion Position:` `Position` is what occurs after the entries are sorted by `Order`, and refers to how many lines/sentences/tokens (depending on settings chosen) the entries are moved from their position in the context. In the example of an Author's Note set to have `-800` priority (in this hypothetical, the "highest" priority) and `-4` insertion, the AN will be placed 3 new lines from the bottom of the context.
  - A positive `Position` value will push the entry down in the context. A positive value remains, to my knowledge, untested. It remains to be seen whether there is potential use for that.

There is an important reason that we want to manipulate the Lorebook and Advanced Context settings.

**INSERTION ORDER:**

From NAI:

> [Insertion Order is] ordered by priority before context is built. Entries with higher [Order] will reserve and use tokens first. If two entries share the same [Order] there is no guarantee which will go first.

In the default Advanced Context Menu, the `Order` for `Story`, `Author's Note`, and `Memory` are:

> | Type           | Value |
> | -------------- | ----- |
> | Memory         | 800   |
> | Story          | 0     |
> | Author's Notes | -400  |

In practice, this means that `Author's Note` is placed at the front, then `Story`, then `Memory`. With the default `Order` setting of 400 for Lorebook entries, the result puts entries at the very back just in front of `Memory`. This leads to an especially problematic scenario when the higher tier `2048` tokens of mostly story overwhelms the context and more difficult characters and concepts can be lost.

At the beginning, OPVAM suggested that `Order` for Lorebook Entries should be set to `0` to avoid placing them in the back of the context with `Memory`. Upon testing, `0` worked. However, there was a side effect. Due to `0` being the same `Priority` as `Story`, I found that sometimes the `Story` and Entries would conflict with where they entered the context. Some generations would put all of the Entries at the very front, literally in front of the output. Others would split an output into two and put them in different parts of the context.

My original solution to this problem was to set the `Order` to `-200.` This placed the entries essentially where directed by the `Position` setting, as it sets entries to a higher priority than `Story` or `Memory`. However, it was limited in effectiveness as it was difficult to control where context items were put into context. From there, OPVAM developed the settings scaffolds referred to in the next section.

**INSERTION POSITION:**

From NAI:

> The location the entry will be inserted into the context. 0 is the very top of the context, 1 is one unit down, 2 is two units down etc. Negative numbers will count from the bottom of the context starting with -1 at the very bottom, making -2 one unit up, -3 two units up etc.

Default `Position` settings for `Story`, `Author Note`, and `Memory` are as follows:

> | Type           | Value |
> | -------------- | ----- |
> | Memory         | 0     |
> | Story          | -1    |
> | Author's Notes | -4    |

`Position` setting for entries is similar to usage of `[t=x]` in EWI. Replace `[t=x]` with `-x`. For example, if you used `[t=9]` as a key for something such as `Theme:`, you could make aim to make similar entry in NAI with `Insertion: -9`.

There is not a significant comment relative to insertion, beside two main things:

- It is not clear whether insertion for non-Story items closer than `-4` is particularly helpful, and may in fact damage coherence. Further testing is needed to determine whether that is a hard limit.
- There is a clear correlation between entries being closer to context and the AI's understanding and incorporation of those entries into the story. Keep that in mind as you tinker settings to your liking.

### 1.1 Scaffolds and Recommended Settings

Scaffolds are simply groups of settings, usually represented in table form, which detail values recommended for the settings (particularly `Position` and `Order`) in the Lorebook and Advanced Context Settings. Scaffolds will be used in this document to convey settings that may be useful for readers.

#### 1.1(a) OPVAM Scaffold

I currently use and recommend OPVAM's scaffold, with some modifications.

**MODIFIED OPVAM SCAFFOLD**

I have made adjustments to OPVAM's original scaffold, which was created prior to more recent discoveries for useful positioning. The modified scaffold takes into account new developments on signposts, story positioning, and my continued success with irregular races lower in context. Please note that `Reserve` would need to be higher for newer caveman formatting, nor have the two been tested together (with the exception of the new form of signpost entry). Please see below this chart for the previous iteration.

> | Position | Order | Reserve | Type                                            | Forced Active? |
> | -------- | ----- | ------- | ----------------------------------------------- | -------------- |
> | -12      | -100  | 200     | Memory                                          | N/A            |
> | -10      | -200  | 100     | Lore: Concepts                                  | No             |
> | -10      | -300  | 100     | Lore: Races                                     | No             |
> | -10      | -400  | 100     | Lore: Places                                    | No             |
> | -10      | -500  | 100     | Lore: Factions                                  | No             |
> | -8       | -600  | 200     | Lore: Story Overview (Themes, weather, setting) | Yes            |
> | -7       | -650  | 200     | Lore: Irregular Races                           | Choice         |
> | -6       | -700  | 100     | Lore: Characters                                | No             |
> | -4       | -800  | 200     | Author's Note                                   | N/A            |
> | -2       | -1000 | 200     | Signpost (`***`, Style, and additional notes)   | Yes            |
> | -1       | 0     | 512     | Story                                           | N/A            |

Note that I marked Irregular Races as a choice. This is due to my finding that, when always active, NAI tends to make reference to species traits and their connection to characters more often, forming what feels like a more cohesive narrative.

**OPVAM ORIGINAL LOREBOOK SCAFFOLD**

While the current scaffold has somewhat evolved, the original scaffold still performs well in Sigurd v3 and is highly recommended.

> | Position | Order | Reserve | Type                                     |
> | -------- | ----- | ------- | ---------------------------------------- |
> | -12      | -100  | 200     | Memory                                   |
> | -10      | -200  | 100     | Lore: Concepts                           |
> | -10      | -300  | 100     | Lore: Races                              |
> | -10      | -400  | 100     | Lore: Places                             |
> | -10      | -500  | 100     | Lore: Factions                           |
> | -8       | -600  | 200     | Lore: Story Overview (forced active)     |
> | -7       | -650  | 200     | Lore: Irregular Races (Kalmarr addition) |
> | -6       | -700  | 100     | Lore: Characters                         |
> | -4       | -800  | 200     | Author's Note                            |
> | -4       | -1000 | 3       | Signpost (Kalmarr addition)              |
> | 0        | 0     | 512     | Story                                    |

From OPVAM:

> Pretty much breaking your author's notes into 2 parts. Story Overview (used to be called Editor's Note) would contain high-level story plot, style, genre, theme etc.. Then you can use your Author's note to steer the story. For example if you wanted an action story with bits of romance your AN would contain this most of the time [ Writing Style: exciting. Genre: action] then change it to [ Genre: romance.] or something like that.

Testing has shown this method to be excellent, both in terms of accuracy and quality of outputs. I use this method consistently since it was recommended, to great effect. My entries are referenced consistently and accurately by the AI, and do not interrupt story flow.

**MODIFIED OPVAM SCAFFOLD**

#### 1.1(b)

OPVAM has recommended a new scaffolding system, developed through further testing on his part. Taking into account the `***` signpost method, he now recommends the following:

**ADVANCED CONTEXT SETTINGS**

> | Name          | Position | Order | Reserve | Insertion Type |
> | ------------- | :------: | :---: | :-----: | -------------- |
> | Story         |    0     |   0   |   512   | Newline        |
> | Memory        |    -1    |  100  |   512   | Newline        |
> | Author's Note |    -4    | -800  |   512   | Newline        |
>
> > **Memory**: Used during playthrough to keep a running summary of the "Story so far". Has a light effect on AI output as it is far from the front/bottom of context. Should be **_intermittently_** updated with story highlights.
> >
> > **Author's Note**: Used to control the flow of the current scene. Position is at -4 from the front/bottom of context, so has a strong effect on output. Should be **_regularly_** updated as the scene changes.

**LOREBOOK CREATION SETTINGS**

> | Name      | Position | Order | Reserve | Search Range | Notes                               |
> | --------- | :------: | :---: | :-----: | :----------: | ----------------------------------- |
> | Concept   |    -1    |  800  |    0    |     2000     | (Multiple)                          |
> | Faction   |    -1    |  700  |    0    |     5000     | (Multiple)                          |
> | Species   |    -1    |  600  |    0    |     2000     | (Multiple)                          |
> | Place     |    -1    |  500  |    0    |     3000     | (Multiple)                          |
> | Character |    -1    |  400  |   200   |     2000     | (Multiple)                          |
> | Brace     |    -8    | -400  |   200   |      -       | (Multiple)                          |
> | Synopsis  |    -8    | -500  |   200   |      -       | (Single, Forced)                    |
> | Pillar    |    -4    | -600  |   200   |      -       | (Multiple)                          |
> | Signpost  |    -4    | -1000 |    3    |      -       | (Single, Forced) - Kalmarr addition |
>
> > From OPVAM:
> >
> > **Synopsis**: Used as an Author's Note that describes the story as a whole. Use tags like Genre, Themes, Setting etc. Previously called "Editor's Note".
> >
> > **Brace**: Any supporting information for concept/faction/species/place/char entries. A brace is typically used to reinforce an idea or concept that the AI has trouble remembering. Can also be used to emphasize important information, ie character/species appearance, worn clothing and motive. Also should be used to describe relationships.
> >
> > **Pillar**: Same idea as a brace, but much closer to the front/bottom of context for crucial information that needs to be highly emphasized.
> >
> > **Notes**: Recommended search ranges have been provided, but it's really something that needs to be treated on a case-by-case basis. For lore with keys that are hard to trigger (or don't trigger often) you may want to increase your search range to ensure the lore stays in context for a longer period of time after each mention.

I do not currently recommend this format, as I believe some tweaking is required. Entries are being injected awkwardly--there may need to be a change to insertion position as with `-1` items are being injected after the story in large quantities.

---

## 2. Lorebook Application (AKA Formatting)

The Lorebook is an incredibly useful function, that can be applied in an almost absurd number of ways. Combined with different Generation Settings, Advanced Context settings, etc., it is very difficult to qualify what the _best_ way of using Lorebooks is. The recommendations I make in this document work for me in my use case. If they do not work for you, you may need to change certain aspects to better fit yours.

Formatting refers, simply, to the syntax one can use in their Lorebook to draft entries in such a way that the AI can understand and apply the contents of entries to the Story. Formats have many forms, but they range from straight descriptive or flowing prose entries (just written normally) or using complicated syntax such as the `{`, `[`, `"` of JSON. Your preference for format may depend on how easy to use you want it to be, how accurate, whether you want the AI to rely on your personal writing style, and other things.

Each format has advantages and disadvantages. I will not discourage anyone from using any format that works for them.

Current formats addressed in this document, or that I intend to address, and which are not inclusive of all those discussed in the NAI Discord or other places, are:

- featherlite (my current preference)
  - Represented by concise, smashed, low-syntax style. Meant to get across ideas for the AI but not impact its writing.
- caveman encapsulated prose
  - Represented by use of short caveman-like entries that cut out unnecessary words (is, that, etc.) and use of `[ ]`. Monky has since updated the format.
- regular encapsulated prose
  - Regular writing describing the entity/concept in the entry, surrounded by `[ ]`.
- regular prose
  - Prose without encapsulation of any kind.
- JSON
  - Syntax-heavy format in style of JSON code: `[{"Entryname":{"key":"value","key1":"value1"}}]`. JSON should be minified using JSONmate or another resource.

Monky suggested that keeping lines to 18 tokens then separating new lines seems to work well. I confirmed that 18 tokens or less for new lines appears to have a positive effect on entries, at least using caveman and featherlite formatting. Reinforcing entries with names on each line is important, and in entries with pronouns appears to help.

I am currently using the featherlite format.

### 2.1 Featherlite

Rinter, the creator of Featherlite, has a wiki that can be found here with all the up to date information on the format in NAI: [Rinter's Featherlite Wiki](https://github.com/RinterWaptor/NAI-research/wiki).

I will not speak in great detail to featherlite's benefits and drawbacks here. Please see Rinter's wiki at the above link for more specific information.

After hiccups with initial testing, where the original `•` syntax starting entries appeared to no longer work, Rinter reworked the format and determined that `[ ]` is acceptable encapsulation for featherlite in NAI. After moving to the new encapsulation, featherlite appears to be a very viable format.

Rinter has since come up with further testing and suggestions for the format. In particular, removing newlines between sections of the entry and replacing them with `;`. The entry will therefor look like:

> `[ Name: age gender race text text Pronoun text; Name text text pronoun text text]`

You can also add a descriptive word to the second part after the `;`, in order to get across an idea that you want to reinforce. For example, you could use `text; Name: behavior`. There is no set list of options, so what works is subject to experimentation. In my experience with featherlite so far, behavior is one of those effective words.

I used featherlite as my primary format in AID, finding that I generally liked its structure and application. I intend to focus quite a bit of my time assisting Rinter with refining its use in NAI. I may eventually draft a separate document on featherlite testing if this document becomes too unwieldy. Additionally, please note that my way of using featherlite may not necessarily match Rinter's fully. I often integrate caveman-like elements into my entries.

#### 2.1(a) Featherlite Testing Note

From initial testing, leaking is incredibly rare and outputs are accurate and high quality, in both play and descriptive testing. I have conducted significant testing since over the past several days and have found that featherlite does not appear to have significant drawbacks. Necessary information is pulled from the entries without inferring writing style. I am finding that the AI is capable of referencing the entries without repitition or incoherence, and in fact is quite capable of connecting entries together in a desireable way. Racial traits are incorporated into the characters, and the characters' relationships with each other are referenced often.

I will undertake comparative testing to determine relative performance once I am comfortable that my current entries are optimized and can be compared properly to optimal entries under other formats. This will most likely occur after I am able to test JSON/python.

**CURRENT TESTING**

I am currently testing the use of `;` at the _end_ of an entry, for example:

> `[ Mark: male wolfkin thickfurofBlack; Mark behavior: kind outgoing; Mark wears: tunic& breeches ];`

I am also testing the use of `and` and `or`, word smashed. Both of these tokenize very well, and seem to tokenize to `|and` and `|or` at the end of most words they are connected to. Rinter noted that `and` is now recommended for featherlite generally, so my testing will merely help determine if it works with the OPVAM scaffold and for my slightly modified entries.

#### 2.1(b) Featherlite Example Entries

_This section is a work in progress, and will be continually updated._

**CHARACTERS**

> Mark (main character of many of my stories):x
>
> > `[ Mark: male wolfkin thickfurOfBlack; Mark behavior: kind outgoing; Mark wears: tunic& breeches ]`

**RACES**

> Wolfkin (primary race in most of my stories):
>
> > `[ wolfkin race: Lupinebody digitigradeBeastkin; wolfkin behavior: expressivetail&ears They friendly ]`

**AUTHOR'S NOTE**

The Author's Note seems to work well with a modified version of featherlite, taking aspects of caveman and other punctuation.

In my experience to date, using new lines and regular featherlite separating categories of Author's Note appears to be less effective than combining them all into a single line entry. Generations follow the direction less effectively, and incoherence increases. As such, I use an Author's note that looks like the following (_updated July 5_).

> Author's Note (Modified Example):
>
> > `[ Author: Terry Pratchett; Tags: romantic& light; Genre: Romance ]`<br>
> > Alternatively, the previous style I used was acceptable:
> > `[ Author: Terry Pratcherr; Tone: romantic& light; WritingStyle: sesquipedalian&& creative ]`
>
> Notes on these examples:
>
> > - I will speak to the benefits of the choices of `Author`, `Tone` (and its alternatives), and `WritingStyle` in the Author's Note section.
> > - `:` syntax: used to denote categories in featherlite. Works for categories in Author's Note--arguably works in other formats as well.
> >   - Rinter has since updated featherlite to recommend use of this syntax for all entries.
> > - `;` syntax: used to separate categories from each other. Not normally used in featherlite. However, in the Author's Note, found it to be an effective way to separate and likely more effective than newlines.
> > - `&` syntax: used to list items within categories, as a replacement of a comma. I have found commas to be ineffective, even weakening list items after the first. This syntax does not leak in this format.
> > - `&&` syntax: appears to be more powerful than a single `&`, and at least has no drawbacks. More work necessary to test its effectiveness.

#### 2.1(c) Featherlite Conversion from AID (with examples)

_No longer being updated--for informational purposes, demonstrating how I originall converted my AID entries to NAI-friendly format._

Following Rinter's new guidelines for Featherlite in NAI, I converted my entries from AID-version to NAI-version. To show this, I will use an example with a race and character I commonly use. Please see [my document](https://github.com/Kalmarr120/Kalmarr_NAI_Public/blob/755de9ae8c29bb7cc8f33d339edfadf395008893/wolfkin_race_featherlite.md) for details on how I constructed the racial entries for AID.

The conversion primarily deals with replacing `•` as preceding syntax, and replacing it with `[ ]` incapsulation. In addition, terms that do not have a significant relation (unlike, for example, hair and hair colour), are separated. Word smashing is kept for related terms in order to potentially maintain their association.

> _My wolfkin race, in AID Featherlite (`EWIJSON`):_
>
> > `•define wolfkin: Lupinebody muzzleBeastkinThey peaceful tribal` \\`[p=5]`<br> `•wolfkin behavior: expressivetail&ears They friendlyopen` \\ `[p=5]`
>
> _Converted to NAI Featherlite (`OPVAM race insertion`):_
>
> > `[ wolfkin: Lupinebody muzzle Beastkin They peaceful tribal ]`<br> `[ wolfkin behavior: expressivetail&ears They friendly open ]`
>
> Applying the principles of new Featherlite, the conversion is minor in this case:
>
> > - `•` encapsulation is removed and replaced with `[ ]`.
> > - `define` is removed. It will need to be tested to determine usefulness in NAI.
> >   - On principle, it should assist the AI with defining a new term, in this case `wolfkin`. The use case may be different from AID.
> > - `Lupinebody` remains smashed, as the intention is to describe their bodies/appearance as "lupine."
> > - `muzzle` is separated from `Beastkin`, as the two terms are not directly related.
> > - `They` is separated from Beastkin, as it is a generic pronoun.
> > - `friendly` is separated from `open`. The two terms are not associated.

To use another example, here is a character entry based on that race:

> Mark, a wolfkin character, in AID Featherlite:
>
> > `• Mark:30♂︎wolfkin lean Hekind joyful` \\ [p=1]<br> `• Mark:Blackfur,White-spot tail,leftearscarHefriendVol` \\ [p=3]
>
> _Converted to NAI Featherlite:_
>
> > `[ Mark: 30 male wolfkin lean He kind joyful]`<br> `[ Mark: Blackfur, White-spot tail, leftearscar He friend Vol]`
>
> The conversion in this case should be a bit more of an obvious example of the new principles.
>
> > - `•` encapsulation is removed and replaced with `[ ]`.
> > - `♂︎` is removed, and replaced with `male`. It is unclear if NAI is able to properly understand and use `♂︎` in the context of this format.
> > - `30`, `male`, and `wolfkin` are broken out into their own words, as they are not associated.
> > - `kind` is broken off from `He`, as they are not associated.
> > - `Blackfur` remains smashed in order to maintain their association.
> > - `leftearscar` is broken off into its own word, as the association is a scar on his left ear.
> > - `He`, `friend`, and `Vol` are broken into separate words.

### 2.2 Monky's Caveman

Caveman was originally developed by Monky in AID. Significant work has been done by Monky on updating the caveman format for NAI. Currently, the format looks like the following:

```
entry:

***

:[ Kizzy plant based extraterrestrial woman nicknamed 'Kiz' ];
:[ Kizzy species Zellan has orange eyes and blue skin ];
:[ Kizzy physiology human-like features attractive ];
:[ Kizzy hair red style short Pixie-Cut ];
:[ Kizzy opaque flesh blue build slender short ];
:[ Kizzy eyes orange her face human-like ];
:[ Kizzy weight 100 pounds height 4'2" ];
:[ Kizzy roles qualified medic pilot engineer mechanic ];
:[ Kizzy behavior blunt diction factual ];
:[ Kizzy wears V5 Sky Maidens jumpsuit ];
:[ Kizzy jumpsuit colored silver and grey with medic insignia ];

```

Monky has confirmed several helpful things to note with this format:

- Each line should be 18 tokens, including encapsulation.
- `:` at the beginning and `;` at the end of the lines can help maintain cohesion and reduce the number of inter-entry leaks. `:[` and `];` are single tokens, so there is not a token downside to this encapsulation.
- `and` and `and with` have been demonstrated to be powerful conecting words, as an alternative to commas or `&`. Avoid the use of commas generally.
- `[ ]` encapsulation with spaces remains the most powerful form of encapsulation for entries in NAI. This is no exception.
- Capitalization of colours and certain other words appears to be extremely helpful with increasing accuracy. This may be due to repetition penalty.
- It is helpful to reinforce the name of the entry on each line. Reinforcing with pronouns mid-line does not appear to be necessary with this method.
- Be mindful of the order of attributes. General information is better to keep at the front/top, such as species, general appearance, etc.

In addition, Monky does not use scaffolded settings, except for a single Author's Note-like entry called a "cue card" that looks like the following:

```
entry:

***

:[ Writing style: Descriptive and creative ];
:[ Do: Describe package explode ];
```

The cue card is placed at `-500` Order and `-2` Position. _Explainer will be added soon._

Finally, Monky uses the following for Memory, placed at `-399` Order:

```
:[PERSPECTIVE: Second person];
:[THEME: Space-faring misadventure];
```

_Explainer for Memory will be added soon._

In order to use the format most closely to Monky's experience, the following settings are recommended:

> | Setting                  | Value    |
> | ------------------------ | -------- |
> | Randomness               | 0.55     |
> | Max Output               | 60       |
> | Min Output               | 20       |
> | Top-K Sampling           | 140      |
> | Nucleus Sampling         | 0.9      |
> | Tail-Free Sampling       | Disabled |
> | Repetition Penalty       | 5        |
> | Repetition Penalty Range | 1536     |
> | Repetition Penalty Slope | 3.06     |

Please note that I have not tested this format and am not able to speak to its strength. However, I trust Monky's testing and relied on his formats in AID, and I believe he can be trusted to develop a strong system that's worthwhile sharing before I have the opportunity to test it personally.

### 2.3 Current Format Testing To-Do

#### 2.3(a) JSON/Python-like

I have seen references to JSON or python-like formatting by members of the NAI Discord. Some appear to be seeing success even with incredibly long entries that would normally go against the conventional wisdom of keeping entries shorter and easier to read by the AI. The reasoning for this is probably connected to the longer context.

I will be testing these formats in their regular style (i.e. with all encapculation and syntax associated), and with the quotation marks removed surrounding the `:`, which is recommended by some of the primary users of the format.

If you do decide to make entries in JSON, I highly recommend writing them in YAML and converting them to JSON. For example, a YAML entry that looks like:

```
Vol:
  age: 30
  gender: male
  species: wolfkin
  fur-color: black
  appearance:
    - tall
    - athletic
```

Once converted into JSON and minified, will look like this:

```
{"Vol":{"age":30,"gender":"male","species":"wolfkin","fur-color":"black","appearance":["tall","athletic"]}}
```

You can then just add `[ ]` encapsulation to the end.

#### 2.3(b) `[ ]` Prose Format

This format appears to work well with caveman/concise prose, and is recommended for users who do not want to fuss with the intricacies of the featherlite format. An example would be:

> `[ Mark age 30 male human knight He strong ]`

Further testing is needed to see how this format behaves with the current recommended settings/Lorebook setup.

#### 2.3(c) Regular Prose Format

Some users on NAI Discord see success using regular Prose, with no encapsulation, as a successful means of formatting Lorebook entries. In my very first interactions and testing with NAI, I tried regular Prose with little success in my use case.

Occult believes that Prose works well when you want to convey the same style in your outputs as in your entries. Prose may not be recommended without encapsulation unless you want that style to transfer to output. This will depend on how you use NAI, your patience, your desire to do creative writing, etc.

Testing of regular prose did not yield success for my use case, either with out without scaffolding. I am not likely to try it again, at least until a larger model is released. Please see other sources, such as the NAI Discord #community-research channel, if you are looking for advice on how to format prose entries

## 3. Story Settings

### 3.1 Generation Settings

_Note: significant discussions on these settings are ongoing and recommendation is likely to change._

I have been working on finding ideal settings for many of the methods used in this guide. Generation settings are probably the most difficult and yet one of the most impactful of the available ways of influencing outputs in NAI. This is a rough estimate of the settings working for me, based on my own experimentation and thoughts from researchers such as Monky and Rinter. I currently recommend an approximation of the following:

**KALMARR SETTINGS**

_Update (July 7):_ I am working on an alternative to these settings, using some adjustments to the repetition penalty. Once settled, I will be moving on to TFS vs Top-K/Nucleus sampling and determining if changes are needed. The below settings are workable but likely to change soon.

I have been working on finding ideal settings for many of the methods used in this guide. Generation settings are probably the most difficult and yet one of the most impactful of the available ways of influencing outputs in NAI. I currently recommend an approximation of the following, based on the settings recommended by Jarel in v3 Sigurd.

With further testing, I have adjusted to using higher TFS of `0.9-0.995`, similar to Rinter's suggestion, from `0.4`.

> | Setting                  |    Value    |
> | :----------------------- | :---------: |
> | Randomness               | 0.55 - 0.65 |
> | Top-K Sampling           |  Disabled   |
> | Nucleus Sampling         |  Disabled   |
> | Tail Free Sampling (TFS) |  0.9-0.995  |
> | Repetition Penalty       |      3      |
> | Repetition Penalty Range |    1472     |
> | Repetition Penalty Slope |  Disabled   |

I have also found some success with using lower randomness and higher TFS, in the past using around `.65` randomness and `.9` TFS. Rinter recommends `.55` randomness and `.995` TFS, which is similar.

My stories have generally been either basic slice-of-life stories, or more NSFW. There is some speculation right now that NSFW or basic stories are better served with TFS rather than Top-K or Nucleus (Top-P) Sampling. If you do not have success with these settings,

### 3.2 Token Banning

Rinter suggested that NAI's token banning may be a useful way of avoiding certain outputs without significantly hampering the AI's ability to use common tokens. This is due to multi-token banning.

Multi-token banning involves banning only instances where tokens are conntected togther directly. For example, if a user wanted to ban possible instances of ` human female`, regular token bans could massively affect outputs due to how common those words are. Instead, by doing a multi-token ban of ` human female`, your ban will only impact cases of those tokens being connected together, making you avoid banning use of ` human` or ` female` entirely. To clarify--the AI in that case will output ` human`, but once it does, it will look for any other token besides ` female`.

---

## 4. Author's Notes

### 4.1 Authors

Following significant testing, `Author` appears to be an extremely powerful tool to influence writing style and story cohesion. This may be due to the finetuning, in which works were tagged in a system that looks like `[ Author: name; Tags: tag1, tag2; Genre: genre ]`. I have tested the following authors and noted success with them:

- `Terry Pratchett`: My favourite, Pratchett invokes a whimsical and light feeling into stories. There is a significant shift in language used. Dialogue is more punchy and dynamic.
- `George R. R. Martin`: GRRM invokes darker feelings and themes, and very descriptive prose. Dialogue is more serious and maintains story cohesion well.
- `Robert Jordan`: Robert Jordan invokes significantly more detailed descriptions.
- `J.K. Rowling`: JKR has a difficult-to-describe style. The descriptions are interesting and dialogue is dynamic.
- `H.P. Lovecraft`:

### 4.2 Writing Styles

_Update (June 29, 2021):_ Zaltys appears to recommend against using `Writing Style` or any variant thereof, due to the way that the data is organized. I will need to conduct testing to determine whether there is a better alternative way of having the same effect. `Tags:` and `Genre:` appear to be recommended. Zaltys suggests using generic terms and ideas like `robot` or `military` or `France` or `1600s`.

Under my current system, all Author's Notes are written in featherlite and placed into the context at Priority `-800` and Insertion `-4`.

_Update (June 27, 2021)_: I have been examining the use of writing styles such as `sesquipedalian` and `creative`, which I have seen used by members of the NAI Discord. These particular styles appear to have significant effects on output.

- `sesquipedalian` was suggested (Cass) as a strong version of `purple prose`. Play testing and descriptive testing appears to confirm that.
- `creative` (Kaelia) appears to encourage the AI to be less repetitive and more varied in its word choices. Lorebook entries are still referred to properly, but the AI is much more likely to choose interesting alternative language when doing so.

Combining these two terms has had a significant impact on how often I need to I now recommend this as the base writing style:

> `[ WritingStyle: sesquipedalian& creative ]`

Further additions that have shown some helpful use (when added to the above), that are otherwise niche, include:

> - `gay`
>   - This style has assisted with avoiding gender changes in gay-focussed stories. It is unclear if it has any other impact on writing.
> - `furry`
>   - This style seems to bring character's non-human attributes into greater focus.
>
> > If added to the base writing style above, these combined would look like:
> >
> > `[ WritingStyle: sesquipedalian& creative& gay& furry ]`

I previously recommended this style, which may still be useful to some:

> `[ WritingStyle: grandiloquent, purple prose]`

#### 4.2(a) Other Writing Style Application Methods

The prefix terms `Writing Style` or `WritingStyle` are not necessarily confirmed to be the most effective ways of applying style to a story. Testing should be done on other terms, such as:

- `Tone:`
- `Style:`
- `Focus:`

### 4.3 Genres, Themes, Etc.

Genres, like Writing Style, are added to the featherlite Author's Note, and may look like this:

> `[ Writing Style: example1& example2; Genre: example3 ]`

This methodology is not finalized, and is subject to ongoing testing. It is the methodology I am currently using in my own play. I am also currently testing multi-line entries that look like the following:

> `[ Author: Name ];`<br> > `[ Tags: item1& item2 ];`<br> > `[ Genre: item1 ];`<br>
>
> While using these, placing `[ WritingStyle: style ]` much closer to the context at `-2`.

Here are Genres, Themes, etc. which I have tested in NAI:

> - `[ Genre: LITEROTICA ]` (_attributed to TravellingRobot's wiki_): when used in conjunction with the recommended writing style seems at least somewhat effective at making interesting outputs and keeping on track for NSFW-focussed stories. Further testing needed to determine magnitude of effect.

Other terms of this type to be tested include:

- `Plot`
- `Scene`
- `Focus`

---

## 5. Person Perspective

It is confirmed that most of the training data uses first and third person, both of which are more effective than second person. To confirm for anyone unaware of the terms, these are:

- First Person: Use of "I," describing the narrative from your perspective.
  - "I looked up at the mountain."
- Second Person: Use of "you," describing the narrative from another person's perspective but referring to you.
  - "You look up at the mountain."
- Third Person: Use of "he/she/they," describing the narrative from the perspective of another person.
  - "He looked up at the mountain."

Person perspective may be in either past or present tense. It is not clear which tense is preferable, but the AI may find past easier as most writing is done in past tense.

There are a couple of methods, though not properly tested, that may be useful to reinforce the person perspective. They are:

> `[ POV: Name/You/I ]`
>
> > `[ protaganist: Name ]`

Both of these can be reasonably used as part of an Author's Note. I have seen a somewhat better retention of person perspective but not strongly enough to fully recommend them.

## 6. Signposts

Extensive testing of signposts has demonstrated that the creation of a "signpost," a forced active Lorebook entry with a group of characters inserted at a specific point to help draw or break the AI's attention, is quite useful. In particular, I recommend using `***`, which the AI knows to be a scene separator. Please see below for more information.

### 6.1 `***` Signposts

Currently, I recommend the placement of a signpost with the following settings:

> Entry:
>
> ```
>
> ***
>
> ```
>
> Order: `-1000`<br>
> Position: `-4`

I am recommending signposts, in particular one signpost of `***` at position `-4` and order `-1000`, based on the below. This applies especially if using OPVAM's settings (defined in this document above) and the featherlite format. The principles are likely to apply with other insertion levels and formats, but personal testing may be required to see what positioning will be effective for you.

**TESTING**

At Monky's suggestion, I tested a single `***` signpost at an position of `-5`. I chose order `-1000`. After some time testing, I also adjusted the signpost entry to include surrounding newlines:

```

***

```

I tested with a simple break test of `Detailed description of Vol: Vol is`, using a character of mine, in addition to existing activated lorebook entries for another character and for my character race. Everything was tested using featherlite. I also underwent significant play testing.

The results of the testing were successful. The AI's generations were generally more accurate, more descriptive, related to the race and the other character, and were less repititive/inclusive of too much information from the prompt/story. When references were made to previous story/prompt context, the descriptions were more creative and tended to expand on those reference (e.g. taking `deep emerald eyes` from the prompt and substituting another trait like `kind` or `forest green`).

Further testing of position `-4` led to better results; more cohesive outputs, and fewer leaks or other errors.

Testing multiple signposts at intervals did not give good results, and the test was abandoned.

### 6.2 `***` In-Entry Signpost

Benvolio mentioned that using `***` within an entry may show some initial promise, based off the use of in-entry signposts in AID, and I therefore decided to test. The method appears as:

> `[ *** Name: entry information here ]`

Testing of this did not yield particularly helpful results. Major segments of the entry were generally ignored.

Benvolio confirmed that his own testing did not have successful results.

### 6.3 `<<•>>>` Signpost

`<<•>>>` was developed by Monky as a signpost for use with EWIJSON in AI Dungeon.

Previously, tests using `<<•>>>` as a signpost was unsuccessful. Additional testing of it may be necessary, as there is a possibility that it was merely inserted into the incorrect position at the time.

### 6.4 Other Signposts

#### 6.4(a) `* * *` Signpost

Recommended by Zaltys as a chapter separator included in training data.

#### 6.4(b) `⁂` Signpost

Recommended by Zaltys as a chapter separator included in training data.

## 7. Other Testing

### 7.1 "Director" Entries

There appears to be some potential benefit with "director" entries, which are short entries telling the AI what to do. These include things like:

> `[ Do: take the book]`
>
> `[ Describe in prose]`

I have not conducted enough research into this to comment on its usefulness at this time. Initial testing shows that `[ Describe in prose]` may have an effect on how the AI outputs information from Lorebook entries.

Some people on NAI Discord report usefulness from this. In particular, the first `[ Do: x]` and similar (`[ Use: x]`, `[ Event: x]`) etc. appear to be able to significantly affect output in a desirable way.

Monky recommends `[ x is currently happening ]`.

### 7.2 Scene Separators

I have done some research on scene separators, and otherwise have tested other scene separators recommended on the NAI Discord.

#### 7.2(a) Asterix Separator

Asterix separators for scenes appears to be relatively powerful, especially combined with newlines. In break testing within an NSFW scene, inputting only a newline, `***`, another newline, and `Mark`, I was getting results such as:

```
[Lewd stuff]

***

Mark woke up the next morning feeling refreshed and rested. He felt like he had a new lease on life. It was a perfect start to a wonderful weekend.
```

An issue that may occur with adding newlines is that the AI may output newlines itself in future generations. Play testing will be necessary to see if this impact is too strong to recommend using `***`.

#### 7.2(b) `<|endoftext|>` Separator

I have performed some testing on the `<|endoftext|>` string that is inputted occasionally into stories, and saw some success.

I found that, although `<|endoftext|>` was generally successful at separating out scenes, the outputs were shorter, less creative, and less cohesive than the recommended `***`.

### 7.3 Input Tools

As certain useful inputs are discovered, they will be added here.

- `I/they/you open[ed] my/their/your mouth to speak`: Discovered by Monky, inputting this can lead to very dramatic and tense dialogue, very dynamic.
- `As if on cue`: I discovered this, borrowing from an AI output of Monky's to see what effect it would have. My testing found that it did create dramatic moments based on the events in the story up to that moment. Like the above, it is a good replacement for the word `suddenly` which can be obnoxious in these stories.

### 7.4 Prompt Generation

A fun way to generate prompts is to use the finetune tagging in an empty context, and generate. That looks like this in the story box (as an example, for an A Song of Ice and Fire based story):

```
[ Author: George R.R. Martin; Tags: dramatic, epic; Genre: Fantasy]     <--- Finetune tagging
[ Event: Jaime Lannister goes to Winterfell ]     <--- Optional "encouragement"
 <--- Press input at the newline here
```

---

## 8. Character/Species "Generator"

From lion:

> The Character / Species generator format for quick use btw
>
> Species Example:
>
> > [ Species: Clefairy ] [ Type: Fairy ]<br> [ Evolution: Clefairy evolves from Cleffa when leveled up with high friendship and evolves into Clefable when exposed to a Moon Stone. ]<br> [ Size: 2 ft | 60 cm (small) ] [ Weight: 15 lb | 8 kg ]<br> [ Biome: Mountains ]<br>
> > Clefairy is a bipedal, pink Pokémon with a chubby, vaguely star-shaped body. A small, pointed tooth protrudes from the upper left corner of its mouth. It has wrinkles beside its black, oval eyes, a single dark pink oval marking on each cheek, and large, pointed ears with brown tips. A tuft of fur curls over its forehead, much like its large, upward-curling tail. Each stocky arm has two small claws and a thumb on each hand and both feet have a single toenail. There is a pair of tiny, butterfly-shaped wings on its back. Though incapable of flight, Clefairy's wings can store moonlight and allow it to float.
>
> Character Example:
>
> > [ Species: Clefairy ] [ Age: 25 ]<br> [ Powers: Can bestow the joy of Pepsi brand cola to all he meets. ]
>
> Of course, feel free to mix and match and add whatever categories you want in the [ CATEGORY: CONTENT ]'s so long as they follow that format

---

## 9. Glossary

This is a glossary of terms used and relied upon in this document. Please feel free to contact me on Discord if you feel a term could use further explanation or is missing from this glossary. I will be updating it on an ad hoc basis.

- Context
  - Author's Note
  - Memory
  - Story
- Formats
  - Cat<<nip>NIP>
  - caveman
  - featherlite
  - JSON
  - python
- Lorebook
- Settings

## 10. Appendix

### 11. Testing Methods (TBC)
