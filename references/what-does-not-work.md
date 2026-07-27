# What does not work

Every trick below circulates as advice. None of them belong in this skill, and it is worth
knowing why, because most of them are worse than doing nothing. Claims here were checked
against primary sources in July 2026; evidence quality is stated per item, because it
varies a lot.

The general shape of the problem: these tricks all try to change the surface of the text
without changing what is in it. Detection that keys on surface can be fooled that way for a
while. Detection that keys on substance cannot, and neither can a reader. Worse, a trick
that fails leaves you holding evidence that you were trying.

## Invisible unicode, homoglyphs, and lookalike scripts

Zero-width spaces sprinkled through the text, Latin `a` swapped for Cyrillic `а`, and
similar character games.

The academic record here is real and cuts both ways, so it deserves the honest version.
Boucher et al.'s "Bad Characters" (IEEE S&P 2022) showed these attacks break unhardened
NLP models, and SilverSpeak (2025) showed homoglyphs collapsing seven research detectors
from useful to worse than chance. But look at who was tested: research baselines, not the
commercial tools people actually face. The same papers hand over the defence, re-render or
normalise the text before scoring, and it is cheap and near-total. The RAID benchmark
found homoglyph attacks cost detectors 40 points on average, with the pointed exception
that GPTZero had already hardened against them. Originality.ai now sells an invisible-text
detector whose whole purpose is to flag these characters as tamper evidence.

That last point is the one that matters. By 2026 the realistic outcome is not "undetected"
but "caught with the one artefact that proves intent." A clumsy sentence is deniable. A
document salted with zero-width joiners is not. It also breaks search, copy-paste, screen
readers, and spellcheck for every legitimate reader.

## Deliberately inserted typos

The theory: human writing has errors, so adding errors makes text look human.

The supporting evidence is a 2023 journalistic test in which one misspelling flipped
Crossplag, a low-tier detector that barely exists any more. Nothing since supports it
against current tools, and current guidance runs the other way: naive obfuscation is
itself a learnable pattern.

The linguistics is the interesting part. Genuine human error is heavily structured:
substitutions cluster on keyboard-adjacent keys, homophone confusions (their/there,
its/it's) come from phonology, and transpositions favour certain letter pairs. Random
injected typos match none of that. Whether *correctly structured* fake typos would work
better has, as far as we could find, never been studied, so anyone asserting it is
guessing. Either way you have made the writing worse, which was supposed to be the thing
you were fixing.

## Thesaurus swapping

Replacing common words with rarer synonyms to raise perplexity.

Perplexity is genuinely a load-bearing feature in older detectors, so the mechanism is not
imaginary. But no credible study isolates thesaurus substitution as an effective evasion
edit, the leading current classifiers have moved beyond raw perplexity precisely because
it is gameable, and the output reads as a person who has swallowed a dictionary. Unusual
*and wrong* is more conspicuous than ordinary and right. What raises perplexity honestly
is a proper noun, a real number, or local jargon, surprising to the model for the correct
reason: it did not know it.

## Humaniser services

Paste in machine text, get back text that scores lower on detectors.

The mechanism is real. Paraphrasing measurably degrades most detectors: DIPPER knocked
DetectGPT from 70.3% to 4.6%, Weber-Wulff's team watched average accuracy drop from about
74% to about 42% after a Quillbot pass, and AuthorMist, a paraphraser trained by
reinforcement learning against live detector APIs, reported 78% to 96% evasion depending
on the target. So the marketing is not entirely fraudulent. Now the rest of it.

The same AuthorMist paper reports that GPTZero and Originality.ai resisted best, even
against a system optimised specifically to beat them. Pangram catches deliberately
humanized academic text at 95% in independent testing. RAID found paraphrasing made one
detector 16 points *more* accurate, because the paraphraser dragged text toward its
training distribution. Independent 2026 head-to-head tests of commercial humanizers
disagree with each other wildly about the same tools in the same months, which tells you
the results are not stable enough to buy. And after all that, what you hold is text that
drifted from what you meant, is odd in a new recognisable way, and still contains zero
facts only you know. You moved a score. You did not make the writing better, and you did
not make it yours.

## Mass find-and-replace on em dashes

Worth flagging honestly since this skill bans em dashes outright.

The folk wisdom turned out to have real numbers behind it, which surprised us. A corpus
study of 69,632 medRxiv preprint discussions found em dash prevalence nearly tripled after
ChatGPT, 4.23% to 11.58%, reaching 20.3% of preprints by 2025, and Altman publicly
acknowledged the habit when announcing the November 2025 fix. One study found that when
you order a model to write plain prose, every other formatting habit collapses but the em
dash survives, the stickiest tell of all.

What does *not* follow is that deleting your em dashes fools a classifier. No study shows
em dash frequency moving a detector verdict on its own; it is one feature among thousands.
And the false-accusation direction is well documented: em dash defenders pointing at
Dickinson are simply right, plenty of skilled humans punctuate this way, and NPR was
covering the "save the em dash" backlash by late 2025. The ban in `SKILL.md` is there
because readers, not classifiers, now pattern-match on it, and because the fight is not
worth having. Do the replacement properly: swapping every dash for a comma produces comma
splices. Two dashes in a sentence usually mean it wants to be two sentences.

## Prompt incantations

Telling the model "write like a human, avoid AI phrases, be undetectable."

Split the claim. Purpose-built adversarial prompting genuinely works in the lab: SICO
(TMLR 2024) cut average detector AUC by 0.5 using optimised in-context examples. But that
is an optimisation loop run against specific detectors, not a sentence you paste. For the
casual version, "write naturally" appended to a normal prompt, we found no controlled
measurement at all. What it observably produces is the model's *idea* of casual, a
recognisable register of its own: more contractions, more exclamation marks, more
"honestly", and exactly the same absence of specifics. The register changed. The substance
did not.

## The quiet assumption under all of these

Every trick above assumes the goal is to move a score. The score is not worth moving.
Detectors flag genuine human writing often enough that universities keep abandoning them,
and miss enough machine text that passing one proves nothing. The only committed reader
who matters is human, and humans key on substance.

## What is left

The interventions with evidence behind them are the boring ones, and they are all things a
good editor would tell you anyway.

Substantive human revision measurably lowers detector scores in the aggregate, direction
confirmed even though no honest study will give you a "revise X% to pass" threshold. Put
in proper nouns, numbers with units, and dates; no study isolates this as an evasion
lever, and we say so in `how-detection-works.md`, but it is what makes writing worth
reading, and it is the one thing no model and no service can supply, because they were not
there. Write in first person about things you actually did. Say what you are unsure of.
Take a position someone could argue with. Cut the discourse markers. Break the parallel
structures, models run three-part constructions at nearly twice the human rate. Let your
sentences swing.

Every one of those makes the writing better on its own terms, which is the test that
matters. If an intervention only helps against a classifier and does nothing for a reader,
it does not belong in your draft.

## Sources

- Boucher et al. Bad Characters: Imperceptible NLP Attacks. IEEE S&P 2022. https://www.cl.cam.ac.uk/~is410/Papers/badchars_draft.pdf
- Creo. SilverSpeak: homoglyph attacks on AI-text detectors. ACL GenAIDetect 2025. https://aclanthology.org/2025.genaidetect-1.1/
- Dugan et al. RAID benchmark (homoglyph and paraphrase attack results). ACL 2024. https://arxiv.org/abs/2405.07940
- Krishna et al. DIPPER paraphrase attack. NeurIPS 2023. https://arxiv.org/abs/2303.13408
- Weber-Wulff et al. Testing of detection tools. IJEI 2023. https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00146-z
- David. AuthorMist: evading detectors with reinforcement learning. 2025. https://arxiv.org/pdf/2503.08716
- Lu et al. SICO: guided evasion via in-context optimisation. TMLR. https://arxiv.org/abs/2305.10847
- Jabarian, Imas. Artificial Writing and Automated Detection. Chicago Booth, 2025. https://bfi.uchicago.edu/insights/artificial-writing-and-automated-detection/
- Pangram third-party evaluations. https://www.pangram.com/blog/third-party-pangram-evals
- Em-ergence of the em-dash (medRxiv corpus study). https://arxiv.org/abs/2606.29540
- The Last Fingerprint: How Markdown Training Shapes LLM Prose. https://arxiv.org/html/2603.27006v1
- TechCrunch. OpenAI fixes ChatGPT's em dash problem. Nov 2025. https://www.techcrunch.com/2025/11/14/openai-says-its-fixed-chatgpts-em-dash-problem/
- NPR. Inside the unofficial movement to save the em dash. Nov 2025. https://www.npr.org/2025/11/10/nx-s1-5596088/inside-the-unofficial-movement-to-save-the-em-dash-from-a-i
- How Persuasive Could LLMs Be? (tricolon frequency). https://arxiv.org/html/2508.09614v1
- Simulating Errors in Touchscreen Typing (human typo structure). https://arxiv.org/pdf/2502.03560
- Originality.ai. Invisible Text Detector & Remover (tamper-flagging). https://originality.ai/blog/invisible-text-detector-remover
