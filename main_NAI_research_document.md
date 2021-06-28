# Format and Customization Research

<details>
<summary> Contents </summary>

### Table of Contents

- [Format and Customization Research](#format-and-customization-research)
    - [Table of Contents](#table-of-contents)
  - [1. Lorebook Settings](#1-lorebook-settings)
    - [1.1 Priority](#11-priority)
    - [1.2 Insertion](#12-insertion)
  - [2. Format Testing](#2-format-testing)
    - [2.1 Featherlite](#21-featherlite)
      - [**2.1(a) Featherlite Conversion (with examples)**](#21a-featherlite-conversion-with-examples)
      - [**2.1(b) Featherlite Testing**](#21b-featherlite-testing)
    - [2.2 Current Format Testing To-Do](#22-current-format-testing-to-do)
      - [2.2(a) JSON/Python-like](#22a-jsonpython-like)
      - [2.2(b) `[ ]` Prose Format](#22b---prose-format)
      - [2.2(c) Regular Prose Format](#22c-regular-prose-format)
      - [2.2(d) `{ }` Prose Format](#22d---prose-format)
      - [2.2(e) futureman](#22e-futureman)
      - [2.2(f) `Cat<NIP>`](#22f-catnip)
  - [3. Story Settings](#3-story-settings)
  - [4. Author's Notes](#4-authors-notes)
    - [4.1 Writing Styles](#41-writing-styles)
    - [4.2 Genres, Themes, Etc.](#42-genres-themes-etc)
    - [4.3 Other Uses](#43-other-uses)
  - [5. Other Testing](#5-other-testing)
    - [5.1 Signposts](#51-signposts)
      - [5.1(a) `***` Signpost](#51a--signpost)
      - [5.1(b) `***` In-Entry Signpost](#51b--in-entry-signpost)
      - [5.1(c) `<<•>>>` Signpost](#51c--signpost)
      - [5.1(d) `* * *` Signpost](#51d----signpost)
      - [5.1(e) `⁂` Signpost](#51e--signpost)
    - [5.2 "Director" Entries](#52-director-entries)
    - [5.3 Scene Separators](#53-scene-separators)
      - [5.3(a) Asterix Separator](#53a-asterix-separator)
      - [5.3(b) `<|endoftext|>` Separator](#53b-endoftext-separator)
    - [6. Glossary](#6-glossary)

</details>
<br>

As a former EWI AID user, finding the best formats to inject context and exploring the ability to inject items into specific places in the context are an important part of my NAI user experience. This page contains information I have learned through testing or the work of others. I will try to credit the original discoverer where possible. Please feel free to reach out on Discord (Kalmarr) if you believe credit is misattributed.

Note that my preferred use case is detailed Lorebook Entries injected relatively close to the context. You can shift your use of `Insertion Position` to be similar to your use in EWI. I speak in further detail in the sections below. My use case is generally due to my preference to use non-human characters in my stories. I expect that simpler use cases with fewer unusual characters/attributes will probably behave better and without as much force.

Testing will not always be described in significant detail, e.g. always including percentage of success/failure for certain things. At this stage, my goal is to test general ways of improving output. I will generall try to describe the result in relative terms (clearer, more accurate, more creative, etc.), compared to other settings/entries. 

----

## 1. Lorebook Settings

The Lorebook has incredibly helpful settings for use in context injection. It is extremely customizable. These are the settings I have found to be the most useful and why. I also address some testing completed.

The primary useful settings to change in Lorebook entries are `Priority` and `Insertion`. The other settings may be referenced in other areas of this guide, or in more detail in the future.

- `Priority` refers to, essentially, the order in which types of context are built in the overall context. The lower the number as an integer (`-700` as an example), the closer to input the priority type is injected into the context. The number is, in essence, completely arbitrary and used as the basis of entries' relative position to each other.
- `Insertion` is what occurs after the entries are sorted by priority, and refers to how many lines/sentences/tokens (depending on settings chosen) the entries is moved from its position in the context. In the example of an Author's Note set to have `-800` priority ("highest" priority) and `-4` insertion, the AN will be placed 3 new lines from the bottom of the context. A positive insertion value will push the entry down in the context.
  - Positive insertion value remains, to my knowledge, untested. It remains to be seen whether there is potential use for that.

### 1.1 Priority

I have updated my suggestion to use `-200` for `Priority`. Instead, I recommend the following, proposed by OPVAM (and updated June 21):

| Position | Priority | Reserve | Type                                    |
| -------- | -------- | ------- | --------------------------------------- |
| -12      | -100     | 200     | Memory                                  |
| -10      | -200     | 100     | Lore: Concepts                          |
| -10      | -300     | 100     | Lore: Races                             |
| -10      | -400     | 100     | Lore: Places                            |
| -10      | -500     | 100     | Lore: Factions                          |
| -8       | -600     | 200     | Lore: Story Overview (forced active)    |
| -6       | -700     | 100     | Lore: Characters                        |
| -4       | -800     | 200     | Author's Note                           |
| 0        | 0        | 512     | Story                                   |


From OPVAM (_New from June 22, 2021_):
> Pretty much breaking your author's notes into 2 parts.  Story Overview (used to be called Editor's Note) would contain high-level story plot, style, genre, theme etc.. Then you can use your Author's note to steer the story.  For example if you wanted an action story with bits of romance your AN would contain this most of the time [ Writing Style: exciting.  Genre: action] then change it to [ Genre: romance.] or something like that.

Testing has shown this method to be excellent, both in terms of accuracy and quality of outputs.

I will be working with priority/insertion as part of testing for Featherlite, and may deviate from this system. I will include that information under my testing for featherlite. see [Rinter's featherlite wiki](https://github.com/RinterWaptor/NAI-research/wiki/Featherlite).

_Update (June 24, 2021):_ Changing insertion/priority under featherlite appears to be unnecessary in my use case (non-human non-standard race and characters). These settings appear to be very effective. I have seen another scaffolding method proposed by Fuzzy which I will review, but am otherwise not likely to experiment further on my own in the near future.

**Older information:**

From NAI:

> Priority Entries are ordered by priority before context is built. Entries with higher priority will reserve and use tokens first. If two entries share the same priority there is no guarantee which will go first.

In the default Advanced Context Menu, the `Priority` for `Story`, `Author's Note`, and `Memory` are:
> **Story:** 0<br/>**Author's Notes:** -400<br/>**Memory:** 800

In practice, this means that `Author's Note` is placed at the front, then `Story`, then `Memory`. With the default `Priority` setting of 400 for Entries, the result puts Entries at the very back just in front of `Memory`. This leads to an especially problematic scenario when the higher tier `2048` tokens of mostly story overwhelms the context.

OPVAM suggested that `Priority` for Lorebook Entries should be set to `0` to avoid placing them in the back of the context with `Memory`. Upon testing, `0` worked. However, there was a side effect. Due to `0` being the same `Priority` as `Story`, I found that sometimes the `Story` and Entries would conflict with where they entered the context. Some generations would put all of the Entries at the very front, literally in front of the output. Others would split an output into two and put them in different parts of the context.

My solution to this problem was to set the `Priority` to `-200.` This places the entries essentially where directed by the `Injection` setting, as it sets Entries to a higher priority than `Story` or `Memory`.

### 1.2 Insertion

 `Insertion` setting for entries is similar to usage of `[t=x]` in EWI. Replace `[t=x]` with `-x`. For example, if you used `[t=9]` as a key for something such as `Theme:`, you could make a similar entry in NAI with `Insertion: -9`.

 My recommended insertion settings are above, under OPVAM's general lorebook settings.

From NAI:

> The location the entry will be inserted into the context. 0 is the very top of the context, 1 is one unit down, 2 is two units down etc. Negative numbers will count from the bottom of the context starting with -1 at the very bottom, making -2 one unit up, -3 two units up etc.

Default `Insertion` settings for `Story`, `Author Note`, and `Memory` are as follows:

> - **Story:** -1
> - **Author Note:** -4
> - **Memory:** 0

_To be expanded on later._

----

## 2. Format Testing

_Updated (June 28, 2021):_ Using `[ ]` instead of `•`, featherlite has shown an excellent ability to avoid leaking (including syntax/mashed words), and at the same time prove to be an effective source of information for the AI. 

I am currently using the featherlite format, as noted in [section 2.1](#21-featherlite).

Alternatively, format testing so far has shown that use of encapsulation `[ .]` or just `[ ]` appears to work well, and works when combined with caveman. E.g.: `[ Mark age 30 male tall he skilled knight]`.

Monky research in NAI Discord suggested that keeping lines to 18 tokens then separating new lines seems to work well.

I have confirmed that 18 tokens or less for new lines appears to be preferable for entries, at least using caveman formatting. Reinforcing entries with names on each line is important.

### 2.1 Featherlite

Rinter, the creator of Featherlite, has a wiki that can be found here with all the up to date information on the format in NAI: [Rinter's Featherlite Wiki](https://github.com/RinterWaptor/NAI-research/wiki).

Initial testing of Featherlite was not necessary promising, due to leaking issues. However, with `•` swapped for `[ ]`, leaking has been tamped down to a minimum and outputs appear to be of good quality. As I did significant amounts of my research using Featherlite in AID, I intend to spend most of my time studying it and ways it can by used in NAI. Initial research will be contained in this document, but I may draft a separate document in the future should using this one become unweildy.

#### 2.1(a) Featherlite Conversion (with examples)

Following Rinter's new guidelines for Featherlite in NAI, I converted my entries from AID-version to NAI-version. To show this, I will use an example with a race and character I commonly use. Please see [my document](https://github.com/Kalmarr120/Kalmarr_NAI_Public/blob/755de9ae8c29bb7cc8f33d339edfadf395008893/wolfkin_race_featherlite.md) for details on how I constructed the racial entries for AID.

The conversion primarily deals with replacing `•` as preceding syntax, and replacing it with `[ ]` incapsulation. In addition, terms that do not have a significant relation (unlike, for example, hair and hair colour), are separated. Word smashing is kept for related terms in order to potentially maintain their association.

>_My wolfkin race, in AID Featherlite (`EWIJSON`):_
>
> > `•define wolfkin: Lupinebody muzzleBeastkinThey peaceful tribal` \\`[p=5]`<br>
> > `•wolfkin behavior: expressivetail&ears They friendlyopen` \\ `[p=5]`
>
>_Converted to NAI Featherlite (`OPVAM race insertion`):_
>
> > `[ wolfkin: Lupinebody muzzle Beastkin They peaceful tribal ]`<br>
> > `[ wolfkin behavior: expressivetail&ears They friendly open ]`
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

>Mark, a wolfkin character, in AID Featherlite:
>
> >`• Mark:30♂︎wolfkin lean Hekind joyful` \\ [p=1]<br>
> >`• Mark:Blackfur,White-spot tail,leftearscarHefriendVol` \\ [p=3]
>
> _Converted to NAI Featherlite:_
> >`[ Mark: 30 male wolfkin lean He kind joyful]`<br>
> >`[ Mark: Blackfur, White-spot tail, leftearscar He friend Vol]`
>
>The conversion in this case should be a bit more of an obvious example of the new principles.
>
> > - `•` encapsulation is removed and replaced with `[ ]`.
> > - `♂︎` is removed, and replaced with `male`. It is unclear if NAI is able to properly understand and use `♂︎` in the context of this format.
> > - `30`, `male`, and `wolfkin` are broken out into their own words, as they are not associated.
> > - `kind` is broken off from `He`, as they are not associated.
> > - `Blackfur` remains smashed in order to maintain their association.
> > - `leftearscar` is broken off into its own word, as the association is >a scar on his left ear.
> > - `He`, `friend`, and `Vol` are broken into separate words.

#### 2.1(b) Featherlite Testing

_This section is currently incomplete_.

From initial testing, leaking is rare and outputs are accurate and high quality. There was only one significant leak of the format style in well over a hundred break tests, e.g:
>`Detailed description of wolfkin: wolfkin are`

_Updated (June 28, 2021):_ I have conducted significant testing, both play and descriptive testing, with featherlite over the past two days. I can now say with some confidence that featherlite works very well and appears to be quite resistant to leaks using current settings. I am finding that the AI is capable of referencing the entries without repitition or incoherence, and in fact is quite capable of connecting entries together in a desireable way. Racial traits are incorporated into the characters, and the characters' relationships with each other are referenced often.

I will undertake comparative testing to determine relative performance once I am comfortable that my current entries are optimized and can be compared properly to optimal entries under other formats. This will most likely occur after I am able to test JSON/python.

>Current examples of WIP entries I am using (as of June 28, 2021) include:
>
>> `[ wolfkin: caninebody digitigrade Beastkin they muzzle ]`<br>
>> `[ wolfkin behavior: expressivetail&ears They friendly peaceful ]` 
>
>> `[ Mark: male wolfkin lean He kind joyful ]`<br>
>> `[ Mark: Blackfur muzzle He bestfriendVol ]`

Please note that my use of featherlite is at least slightly different from the version usually proposed by Rinter, in that I rely on other punctuation such as `&` a bit more often (like in my Author's Note example further down). I also tend to mash words less frequently, making my entries slightly more similar to caveman.

### 2.2 Current Format Testing To-Do

#### 2.2(a) JSON/Python-like

I have seen references to JSON or python-like formatting by members of the NAI Discord. Some appear to be seeing success even with incredibly long entries that would normally go against the conventional wisdom of keeping entries shorter and easier to read by the AI. The reasoning for this is probably connected to the longer context.

I will be testing these formats in their regular style (i.e. with all encapculation and syntax associated), and with the quotation marks removed surrounding the `:`, which is recommended by some of the primary users of the format.

#### 2.2(b) `[ ]` Prose Format

This format appears to work well with caveman/concise prose, and is recommended for users who do not want to fuss with the intricacies of the featherlite format. An example would be:

>`[ Mark age 30 male human knight He strong]`

Further testing is needed to see how this format behaves with the current recommended settings/Lorebook setup.

#### 2.2(c) Regular Prose Format

Some users on NAI Discord see success using regular Prose, with no encapsulation, as a successful means of formatting Lorebook entries. In my very first interactions and testing with NAI, I tried regular Prose with little success in my use case. However, I have not tested regular Prose with my current settings/Lorebook setup, and results may differ now. Further testing is necessary.

Occult believes that Prose works well when you want to convey the same style in your outputs as in your entries. Prose may not be recommended without encapsulation unless you want that style to transfer to output. This will depend on how you use NAI, your patience, your desire to do creative writing, etc.

#### 2.2(d) `{ }` Prose Format

Initial testing did not show `{ }` as superior to `[ ]`. Testing for this method of encapsulation is on permanent hiatus. So far appears to have been dropped by serious testers, outside of JSON or python-like formats.

#### 2.2(e) futureman

Due to the success of the caveman format, futureman appears to no longer fit the particular niche that it did in AID.

#### 2.2(f) `Cat<NIP>`

I am putting `Cat<NIP>` on permanent hiatus Due to my preference to focus on either caveman/featherlite-oriented formats.

## 3. Story Settings

I am currently using a modified version Monky's suggested story settings.

Updated settings based on Monkys suggestions (_June 28, 2021_):

Only changes to default recommended by Monky are Tail-Free Sampling set to `0.5`, Top-K Sampling `disabled`. So far seeing success combined with signpost and featherlite formatting. I have found that decreased randomness is necessary as well, and am generally using `0.7`.

_Updated (June 28, 2021):_ I am now conducting tests using Tail-Free Sampling set to `0.992` and will post results here once ready. 

----

## 4. Author's Notes

### 4.1 Writing Styles

Under my current system, all Author's Notes are written in featherlite and placed into the context at Priority `-800` and Insertion `-4`.

_Update (June 27, 2021)_: I have been examining the use of writing styles such as `sesquipedalian` and `creative`, which I have seen used by members of the NAI Discord. These particular styles appear to have significant effects on output.

- `sesquipedalian` was suggested (Cass) as a strong version of `purple prose`. Play testing and descriptive testing appears to confirm that.
- `creative` (Kaelia) appears to encourage the AI to be less repetitive and more varied in its word choices. Lorebook entries are still referred to properly, but the AI is much more likely to choose interesting alternative language when doing so.

Combining these two terms has had a significant impact on how often I need to  I now recommend this as the base writing style:

>`[ WritingStyle: sesquipedalian& creative ]`

Further additions that have shown some helpful use (when added to the above), that are otherwise niche, include:
> - `gay`
>   - This style has assisted with avoiding gender changes in gay-focussed stories. It is unclear if it has any other impact on writing.
> - `furry`
>   - This style seems to bring character's non-human attributes into greater focus.
>
>>If added to the base writing style above, these combined would look like: 
>>
>>`[ WritingStyle: sesquipedalian& creative& gay& furry ]` 

I previously recommended this style, which may still be useful to some:

>`[ WritingStyle: grandiloquent, purple prose]`

### 4.2 Genres, Themes, Etc.

Genres, like Writing Style, are added to the featherlite Author's Note, and may look like this:

> `[ Writing Style: example1& example2; Genre: example3 ]`

This methodology is not finalized, and is subject to ongoing testing. It is the methodology I am currently using in my own play.

Here are Genres, Themes, etc. which I have tested in NAI:

> - `[ Genre: LITEROTICA ]` (_attributed to TravellingRobot's wiki_): when used in conjunction with the recommended writing style seems at least somewhat effective at making interesting outputs and keeping on track for NSFW-focussed stories. Further testing needed to determine magnitude of effect.

### 4.3 Other Uses

TBC

----

## 5. Other Testing

### 5.1 Signposts

#### 5.1(a) `***` Signpost

_Updated (June 27, 2021):_ Follow-up testing of signposts has demonstrated that, in fact, `-4` may be a preferable insertion position for the signpost, which puts it right after the Author's Note. I will keep the below for now and will update to reflect that later. Please keep in mind while reading that `-4` is the recommendation, and not `-5`.

_Further Updated (June 27, 2021):_ Further testing of before-entries signposts has not yielded successful results. Noticed lowered cohesion and a general worsening of quality/creativity in the outputs. In addition, multiple signposts at varied locations in the context do not appear to have had a positive effect on outputs, with similar (although not as severe) impacts as before-entry signposts. May conduct further testing, but for now one signpost at `-5` and `-1000` appears to be preferable for recommended use.

I am recommending signposts, in particular one signpost of `***` at insertion ~~`-5`~~ `-4` and priority `-1000`, based on the below. This applies especially if using OPVAM's settings (defined in this document above) and the featherlite format. The principles are likely to apply with other insertion levels and formats, but personal testing may be required to see what positioning will be effective for you.

My testing was first done with default settings and 0.6 randomness, then Monky's settings (I may be adjusting this recommendation--testing ongoing. See section 3. for information):
> Randomness: `0.8`<br>
> Top-K Sampling: `disabled`<br>
> Nucleus Sampling: `disabled`<br>
> Tail-Free Sampling: `0.5`<br>
> Repitition Penalty: `1.2`<br>
> Repitition Penalty Range: `512`<br>
> Repitition Penalty Slope: `4.05`<br>

At Monky's suggestion, I tested a single `***` signpost at an insertion of `-5`. I chose a priority of `-1000`. After some time testing, I also adjusted the signpost entry to include surrounding newlines:

```

***

```

I tested with a simple break test of `Detailed description of Vol: Vol is`, using a character of mine, in addition to existing activated lorebook entries for another character and for my character race. Everything was tested using featherlite.

The results of the testing were successful. The AI's generations were generally more accurate, more descriptive, related to the race and the other character, and were less repititive/inclusive of too much information from the prompt/story. When references were made to previous story/prompt context, the descriptions were more creative and tended to expand on those reference (e.g. taking `deep emerald eyes` from the prompt and substituting another trait like `kind` or `forest green`). 

#### 5.1(b) `***` In-Entry Signpost

Benvolio mentioned that using `***` within an entry may show some initial promise, based off the use of in-entry signposts in AID, and I therefore decided to test. The method appears as:
> `[ *** Name: entry information here ]`

Testing of this did not yield particularly helpful results. Major segments of the entry were generally ignored.

Benvolio confirmed that his own testing did not have successful results.

#### 5.1(c) `<<•>>>` Signpost

`<<•>>>` was developed by Monky as a signpost for use with EWIJSON in AI Dungeon. 

Previously, tests using `<<•>>>` as a signpost was unsuccessful. Additional testing of it may be necessary, as there is a possibility that it was merely inserted into the incorrect position at the time.

#### 5.1(d) `* * *` Signpost

Recommended by Zaltys as a chapter separator included in training data.

#### 5.1(e) `⁂` Signpost

Recommended by Zaltys as a chapter separator included in training data.

### 5.2 "Director" Entries

There appears to be some potential benefit with "director" entries, which are short entries telling the AI what to do. These include things like:

>`[ Do: take the book]`
>
>`[ Describe in prose]`

I have not conducted enough research into this to comment on its usefulness at this time. Initial testing shows that `[ Describe in prose]` may have an effect on how the AI outputs information from Lorebook entries.

Some people on NAI Discord report usefulness from this. In particular, the first `[ Do: x]` and similar (`[ Use: x]`, `[ Event: x]`) etc. appear to be able to significantly affect output in a desirable way.

### 5.3 Scene Separators

I have done some research on scene separators, and otherwise have tested other scene separators recommended on the NAI Discord.

#### 5.3(a) Asterix Separator

Asterix separators for scenes appears to be relatively powerful, especially combined with newlines. In break testing within an NSFW scene, inputting only a newline, `***`, another newline, and `Mark`, I was getting results such as:

```
[Lewd stuff]

***

Mark woke up the next morning feeling refreshed and rested. He felt like he had a new lease on life. It was a perfect start to a wonderful weekend.
```

An issue that may occur with adding newlines is that the AI may output newlines itself in future generations. Play testing will be necessary to see if this impact is too strong to recommend using `***`.

#### 5.3(b) `<|endoftext|>` Separator

I have performed some testing on the `<|endoftext|>` string that is inputted occasionally into stories, and saw some success. 

I found that, although `<|endoftext|>` was generally successful at separating out scenes, the outputs were shorter, less creative, and less cohesive than the recommended `***`.

----

### 6. Glossary

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
