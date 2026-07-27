# What does not work

Every trick below circulates as advice. None of them belong in this skill, and it is worth
knowing why, because most of them are worse than doing nothing.

The general shape of the problem: these tricks all try to change the surface of the text
without changing what is in it. Detection that keys on surface can be fooled that way for a
while. Detection that keys on substance cannot, and neither can a reader. Worse, a trick
that fails leaves you holding evidence that you were trying.

## Invisible unicode

Zero-width spaces, zero-width joiners, and other non-printing characters sprinkled through
the text to disrupt tokenisation.

This fails on contact. Any pipeline that normalises unicode strips them before analysis, and
that is most pipelines. Meanwhile the characters sit in your document as a plain,
machine-readable record of deliberate tampering, which is a far worse position than an
awkward paragraph. There is no version of getting caught at this that goes well.

## Homoglyphs and Cyrillic lookalikes

Replacing Latin `a` with Cyrillic `а`, `e` with `е`, and so on.

Same failure, more detectable. Mixed-script text is trivially flagged by a script-consistency
check, which takes about four lines of code. It also breaks search, copy-paste, screen
readers, and spellcheck. You are degrading the document for every legitimate reader in order
to fool a classifier that would have caught it anyway.

## Deliberately inserted typos

The theory is that human writing has errors, so adding errors makes text look human.

Human error is not randomly distributed. It clusters around homophone confusion, doubled
words at line breaks, agreement failures in long sentences, and the specific keys next to the
intended one. Randomly injected typos look nothing like this, and a classifier trained on
real human text has seen far more of the real distribution than you have.

There is also the obvious point. You were trying to make the writing better. This makes it
worse.

## Thesaurus swapping

Replacing common words with rarer synonyms to raise perplexity.

This does raise perplexity, and it raises it in a way that reads as a person who has
swallowed a dictionary. Word choice that is unusual *and* wrong is more conspicuous than word
choice that is ordinary and right. What actually raises perplexity honestly is a specific
proper noun, a real number, or a piece of local jargon, because those are surprising to a
model for the correct reason: it did not know them.

## Humaniser services

Paste in machine text, get back text that scores lower on detectors.

Mostly these are paraphrasers, and paraphrasing does measurably degrade detector performance
(see Krishna et al. in `how-detection-works.md`, which built one specifically to demonstrate
it). So the claim is not fraudulent. The problem is what you are left with: text that is
now odd in a new and recognisable way, that has drifted from what you meant, and that still
contains zero facts only you know. You have moved a score. You have not made the writing
better and you have not made it yours.

They also produce a second-order tell. Recursively paraphrased text has a characteristic
flatness of its own, and detectors are trained on their output now.

## Mass find-and-replace on em dashes

Worth flagging honestly since this skill bans em dashes outright.

I have not seen a study establishing that em dash frequency alone materially moves a
classifier score, and I would not expect it to. As a single feature among thousands it is
nearly noise. The rule in `SKILL.md` is not there for the classifier. It is there because the
em dash became a folk signal that human readers now react to, fairly or not, and readers are
the audience that matters. Do not mistake it for a technical countermeasure.

The same honesty applies to a swap done badly. Replacing every em dash with a comma produces
comma splices and sentences that lose their joints. Restructure instead. Two dashes in a
sentence almost always mean it wants to be two sentences.

## Keyword stuffing and prompt gaming

Padding text with domain terms, or instructing the model to "write undetectably".

Asking a model to write undetectably mostly produces its idea of casual writing, which is a
recognisable register of its own: more contractions, more exclamation marks, more "honestly",
and exactly the same absence of specifics. The register changed. The substance did not.

## What is left

The interventions with evidence behind them are the boring ones, and they are all things a
good editor would tell you anyway.

Raise burstiness by letting one thought run long and stopping the next one short. Put in
proper nouns, numbers with units, and dates. Write in first person about things you actually
did. Say what you are unsure of. Take a position someone could argue with. Cut the discourse
markers. Break the parallel structures.

Every one of those makes the writing better on its own terms, which is the test that matters.
If an intervention only helps against a classifier and does nothing for a reader, it does not
belong in your draft.
