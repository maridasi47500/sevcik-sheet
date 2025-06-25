\version "2.22.1"

violinPart = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Sample phrase from a Frescobaldi-style passage
  a4^\markup { "espressivo" }^1 \downbow
  b^2 \upbow
  c^3 \downbow
  d^1 \upbow
  e^2 \downbow
  f^4 \upbow
  g^1 \downbow
  a^3 \upbow
}

violinPartA = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % One bow stroke for these notes (slur)
  a4^1 (\downbow b^2 c^3 d^1 )

  % New stroke begins here
  ( e^2 \upbow f^4 g^1 a^3 )
}

violinPartB = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  a4^1^\markup { "fr." } % tirer
  b^2^\markup { "sp." } % pousser
  ( c^3 d^1^\markup { "FR" } )
  ( e^2^\markup { "SP" } f )
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinPart
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinPartA

}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinPartB

}

barPattern = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Variante 1 - Slur + upbow
  \repeat volta 1 {
    \once \override DynamicText.color = #red
    ( a4^1 b^2 c^3 d^1 ) \upbow
    \f
  }

  % Variante 2 - No slur + downbow + decrescendo
  \repeat volta 1 {
    a4^1 \downbow \> 
    b^2 c^3 d^1 \!
    \p
  }

  % Variante 3 - Mixed dynamics + slur + upbow
  \repeat volta 1 {
    \mf ( a4^1 b^2 ) \upbow
    \> c^3 d^1 \!
    \pp
  }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \barPattern
}

pattern = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1: Ascending with fingering and crescendo
  \once \override DynamicText.color = #blue
  \once \override Fingering.direction = #UP
  \once \override Script.color = #darkgreen
  \dynamicUp
  \> 
  a4^1 b^2 c^3 d^4
  \!

  % Bar 2: Mirror (descending inversion) with fingering and piano
  \p
  d4^4 c^3 b^2 a^1
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \pattern
}
\version "2.24.2"

\version "2.24.2"

ascendingMirrorStudy = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1: Ascending with wide intervals, crescendo and fingerings
  \once \override Fingering.direction = #UP
  \dynamicUp
  \> 
  a4^1 c'^3 f^4 a^4
  \!
  \dynamicDown

  % Bar 2: Mirrored (descending), with opposite fingerings and dynamic drop
  \once \override Fingering.direction = #DOWN
  \p
  a^4 f^3 c^2 a'^1
}

\score {
  \new Staff \with {
    instrumentName = " demanche"
  } \ascendingMirrorStudy
}

violinTriplets = \relative c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1: Three triplets, mixed bowings
  \tuplet 3/2 { a8^1 \downbow b^2 \upbow c^3 }
  \tuplet 3/2 { d^4 \downbow e^1 \upbow f^2 }
  \tuplet 3/2 { g^3 \upbow a^4 \downbow }
  \tuplet 3/2 { b^1 \downbow c^2 \upbow }

  % Bar 2: Repeat with variation in notes and bowings
  \tuplet 3/2 { f8^2 \upbow g^3 \downbow a^4 }
  \tuplet 3/2 { c^1 \downbow b^2 \upbow a^1 }
  \tuplet 3/2 { g^3 \upbow f^2 \downbow }
  \tuplet 3/2 { e^1 \downbow d^2 \upbow }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinTriplets
}

violinIntervals = \absolute c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1: Wide leaps up (A string)
  \mf
  \once \override Fingering.direction = #UP
  a4^1 c'^3 e'^4 a'^4

  % Bar 2: Mirror descent
  \p
  a'^4 e'^3 c'^2 a^1

  % Bar 3: Slight variation—ascending 6th, 7th, octave
  \> 
  a4^1 f'^4 g'^4 a'^4
  \!

  % Bar 4: Mirror
  \pp
  a'^4 g'^3 f'^2 a^1
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinIntervals
}

violinExercise = \absolute c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1 – Ascending wide intervals on A string, slurred, downbow
  \once \override Fingering.direction = #UP
  \once \override Script.color = #darkgreen
  ( a4^1 \downbow c'^3 f'^4 a'^4 )

  % Bar 2 – Mirror: descending intervals, same string, upbow
  \once \override Fingering.direction = #UP
  ( a'^4 \upbow f'^3 c'^2 a^1 )

  % Bar 3 – Two-string double stops with dynamics
  \mf
  <a^1 f'^4>4 \downbow
  <b^2 g'^3> \upbow
  <g^3 a'^4> \downbow
  <g^4 d'^4> \upbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinExercise
}

violinEtude = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4
  \once \override Fingering.direction = #UP

  % Bar 1 – Slur + downbow, accent on 1st note
  (
    \accent a4^1 \downbow
    b^2
  )
  c^3 \upbow
  d^4 \downbow

  % Bar 2 – All accented, alternate bowings
  \accent e^1 \upbow
  \accent f^2 \downbow
  \accent g^3 \upbow
  \accent a^4 \downbow

  % Bar 3 – Slur middle pair, mixed bowings
  b^1 \upbow
  (
    c^2 d^3
  )
  e^4 \downbow

  % Bar 4 – Heavy accents and bow flips
  \accent \downbow f^1
  \accent \upbow g^2
  a^3
  \accent \downbow b^4
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinEtude
}

violinStudy = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1 – Whole bow, sautillé, on the A string
  \once \override TextScript.padding = #2
  a4^\markup { "Whole Bow – III" } \downbow
  b8-. \upbow c-. \downbow d-. \upbow
  \once \override TextScript.padding = #2
  e4^\markup { "Springing Bow – II" } \upbow

  % Bar 2 – Half bow + pause + pizzicato
  f4^\markup { "1st Half Bow" } \downbow
  \breathe
  \once \override TextScript.padding = #2
  g4^\markup { "pizz." }
  <a c'>8^\markup { "II" } \upbow <b d'>8 \downbow

  % Bar 3 – Trill, harmonic, finger lift
  \once \override TextScript.padding = #2
  a4^\markup { "Trill + Lift 2nd Finger" } \trill \downbow
  \once \override TextScript.padding = #2
  g'4^\markup { "Flautato (IV)" } \harmonic
  \once \override TextScript.padding = #2
  r2^\markup { "Stop – Remove left hand from fingerboard" }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinStudy
}
heythere = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4

  <d\harmonic a'>4
  <d a'\harmonic>4


}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \heythere
}

sixthStudy = \absolute c' {
  \clef treble
  \key d \minor
  \time 4/4

  % Bar 1 – Ascending sixths by 2 steps, with slurs and bowing
  \once \override Fingering.direction = #UP
  \mf
  ( b4^2 \downbow g'^4 )   % minor sixth
  ( d^1 \upbow b'^4 )      % major sixth

  % Bar 2 – Descending sixths, mirror, dynamic contrast
  \p
  ( a'^4 \downbow f^2 )    % major sixth
  ( c'^3 \upbow a^1 )      % minor sixth

  % Bar 3 – Mixed direction with accents, no open string
  \accent \downbow d^1
  ( b'^4 \upbow )
  \accent f^2
  ( a'^4 \downbow )

  % Bar 4 – Crescendo and bow control
  \once \override DynamicText.color = #blue
  \> 
  ( g^2 \upbow e'^4 )
  ( b^1 \downbow g'^4 )
  \!
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \sixthStudy
}
\version "2.24.2"

sixthsDoubleStop = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4

  \once \override Fingering.direction = #UP

  % Double stops in sixths, no open strings, with bowing
  <b^2 g'^4>4 \downbow
  <c^3 a'^1> \upbow
  <d^1 b'^4> \downbow
  <e^2 c'^3> \upbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \sixthsDoubleStop
}

violinGlideStudy = {
  \clef treble
  \key d \minor
  \time 3/4

  % Bar 1 – Slow uniform glissando (up-bow)
  \once \override TextSpanner.bound-details.left.text = "Glissando"
  \once \override Fingering.direction = #UP
  \once \override TextSpanner.style = #'solid
  d'4^3 \startTextSpan \upbow
  ~ d'4
  ~ d'4 \stopTextSpan

  % Bar 2 – Ricochet effect (down-bow), staccato bounces
  \once \override TextScript.padding = #2
  \once \override Fingering.direction = #UP
  e'8^3-. \downbow
  f'-. g'-. f'-.
  e'-. d'-. c'-.

  % Bar 3 – Slow return glissando, same finger, up-bow
  \once \override TextSpanner.bound-details.left.text = "Return Glide"
  d'4^3 \startTextSpan \upbow
  ~ d'4
  ~ d'4 \stopTextSpan
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinGlideStudy
}

glissandoRicochetStudy = {
  \clef treble
  \key d \minor
  \time 3/4

  % Bar 1 – Descending glissando: High D to low E, single bow
  \once \override TextSpanner.bound-details.left.text = "Glissando: D'' to E"
  \once \override TextSpanner.style = #'solid
  \once \override Fingering.direction = #UP
  d''4^3 \downbow \startTextSpan
  ~ d''4
  ~ e'4 \stopTextSpan

  % Bar 2 – Ricochet: from D'' downward
  \once \override TextScript.padding = #2
  \once \override Fingering.direction = #UP
  \once \override Script.color = #darkred
  \accent \downbow d''8^3-.
  b'-. a'-. f'-.
  \once \override TextScript.padding = #2
  e'^3^\markup { "Ricochet" }-.

  % Bar 3 – Ricochet up from low E (optional variant)
  \once \override Fingering.direction = #UP
  \upbow e'8^1-. g'-. b'-. d''-. 
  f''^3-. \downbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \glissandoRicochetStudy
}

longGlissando = \absolute {
  \clef treble
  \key d \minor
  \time 3/4

  % Continuous sixteenth-note glissando across register

  \once \override TextSpanner.bound-details.left.text = "Glissando – 3rd Finger"
  \once \override TextSpanner.style = #'solid
  \once \override TextSpanner.bound-details.right.padding = 1
  \once \override Fingering.direction = #UP

  \absolute c'' {
    16^3 \startTextSpan  g a bes b c' d' e' f' g' \stopTextSpan
  }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \longGlissando
}

violinOctaveStudy = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4
  \once \override Fingering.direction = #UP

  % Bar 1 – Original melody
  a4^1 b^2 c^3 d^4

  % Bar 2 – Octave double stops (no open strings)
  <a a'>^1 \downbow
  <b b'>^2
  <c c'>^3
  <d d'>^4
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinOctaveStudy
}

ricochetExercise = \relative c''' {
  \clef treble
  \key d \minor
  \time 7/8

  \once \override DynamicText.color = #blue
  \once \override Hairpin.to-barline = ##f
  \once \override Fingering.direction = #UP

  % Début pianissimo avec crescendo et ricochet (1 seul coup d'archet)
  \pp
  \downbow
  \tuplet 14/8 {
    d32^3 e f d c b a g f e d c b a
  }
  \f
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \ricochetExercise
}

glissandoRicochetExercise = \relative c''' {
  \clef treble
  \key d \minor
  \time 7/8

  % Bar 1 – Ricochet
  \once \override Fingering.direction = #UP
  \pp
  \<
  \downbow
  \mark \markup { \box "Ricochet" }
  \tuplet 14/8 {
    ( d32^3 e f d c b a g f e d c b a )
  }

  % Bar 2 – Glissando
  \mark \markup { \box "Glissando" }
  \tuplet 14/8 {
    ( d32 e f d c b a g f e d c b a )
  }
   
  \f
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \glissandoRicochetExercise
}


fourVoiceDirections = \absolute c {
  \clef treble
  \key d \minor
  \time 2/4

  % a) Both chords descending
  \mark \markup { \bold "a) Descending – Descending" }
  <g' f d b>4\arpeggio \downbow
  <e c a f>4\arpeggio \upbow

  % b) Both chords ascending
  \mark \markup { \bold "b) Ascending – Ascending" }
  <b d f' g'>4\arpeggio \downbow
  <c e a' b'>4\arpeggio \upbow

  % c) First chord ascending, second descending
  \mark \markup { \bold "c) Ascending – Descending" }
  <a c f' a'>4\arpeggio \downbow
  <d b g e>4\arpeggio \upbow

  % d) First chord descending, second ascending
  \mark \markup { \bold "d) Descending – Ascending" }
  <g f d b>4\arpeggio \downbow
  <b d f' a'>4\arpeggio \upbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \fourVoiceDirections
}


fourVoiceMotionStudy = \absolute c {
  \clef treble
  \key d \minor
  \time 2/4

  % a) Both chords descending
  \mark \markup { \bold "a) Descending – Descending" }
  <g' f d b>4\arpeggio \downbow
  <e c a f>4\arpeggio \upbow

  % b) Both chords ascending
  \mark \markup { \bold "b) Ascending – Ascending" }
  <b d f' g'>4\arpeggio \downbow
  <c e g' a'>4\arpeggio \upbow

  % c) First ascending, second descending
  \mark \markup { \bold "c) Ascending – Descending" }
  <a c f' a'>4\arpeggio \downbow
  <d b g e>4\arpeggio \upbow

  % d) First descending, second ascending
  \mark \markup { \bold "d) Descending – Ascending" }
  <f d b g>4\arpeggio \downbow
  <a c e' g'>4\arpeggio \upbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \fourVoiceMotionStudy
}

violinFourVoiceVariants = \relative c {
  \clef treble
  \key d \minor
  \time 2/4

  % a) Both chords descending
  \mark \markup { \bold "a) Descending – Descending" }
  <g f d b>4\arpeggio \downbow
  <e c a f>4\arpeggio \upbow

  % b) Both chords ascending
  \mark \markup { \bold "b) Ascending – Ascending" }
  <b d f' g'>4\arpeggio \downbow
  <c e g' a'>4\arpeggio \upbow

  % c) Ascending – Descending
  \mark \markup { \bold "c) Ascending – Descending" }
  <a c f' a'>4\arpeggio \downbow
  <d b g e>4\arpeggio \upbow

  % d) Descending – Ascending
  \mark \markup { \bold "d) Descending – Ascending" }
  <f d b g>4\arpeggio \downbow
  <a c e' g'>4\arpeggio \upbow
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinFourVoiceVariants
}
\version "2.24.2"

\header {
  title = "Étude on Arpeggiated Harmony and String Color"
  subtitle = "For Four-Voice Voicings Across the Violin Range"
  composer = "for Solo Violin"
}

fourVoiceEtude = \absolute c {
  \clef treble
  \key d \minor
  \time 2/4

  \once \override Fingering.direction = #UP
  \once \override StringNumber.direction = #DOWN

  % Phrase 1 – Soft entry, clear string placement, open string shift
  \pp
  <g\4^1 b\3^2 d'\2^3 g'\1^4>4\arpeggio \downbow
  <a\4^1 c'\3^2 e'\2^3 a'\1^4>4\arpeggio \upbow

  % Phrase 2 – Dynamic growth
  \mp
  <bes\4^1 d'\3^2 f'\2^3 bes'\1^4>4\arpeggio \downbow
  <c'\4^1 e'\3^2 g'\2^3 c''\1^4>4\arpeggio \upbow

  % Phrase 3 – Tricky intonation (with harmonic color)
  \mf
  <d'\4^1 a'\3^\markup { "harmonic" } f''\2^3 d'''\1^4>4\arpeggio \downbow
  <e'\4^1 g'\3^2 c''\2^3 e'''\1^4>4\arpeggio \upbow

  % Phrase 4 – Open string base for brilliance
  \f
  <a\4^0 c'\3^2 e'\2^3 a'\1^4>4\arpeggio \downbow
  <g\4^0 b\3^2 d'\2^3 g'\1^4>4\arpeggio \upbow

  % Phrase 5 – Back to softness with shimmer (flautato optional)
  \pp
  < a\3^2 c'\2^3 f'\1^4 a'\4^1>4\arpeggio \upbow
  < g\3^2 b\2^3 e'\1^4 g'\4^1>4\arpeggio \downbow

  % Final cadence – crescendo to full tone
  \> 
  <d\4^1 f'\3^2 a'\2^3 d''\1^4>4\arpeggio \downbow
  <g\4^1 b\3^2 d'\2^3 g'\1^4>4\arpeggio \upbow
  \ff
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \fourVoiceEtude
}

violinBowGymnastics = \absolute c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Four triplets, 3 notes each = 12 notes
  \tuplet 3/2 {
    % Triplet 1
    \downbow a16-. \upbow b-. \downbow c'-.

    % Triplet 2
    \upbow d'-. \downbow c'-. \upbow b-.

    % Triplet 3
    \downbow a-. \upbow g-. \downbow f'-.

    % Triplet 4
    \upbow e'-. \downbow d'-. \upbow c'-.
  }
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \violinBowGymnastics
}

oneChordTexture = \absolute c {
  \clef treble
  \key d \minor
  \time 4/4

  % Arpeggiated 4-part chord in croches
  \downbow
    a4\2^3 d'\1^4 f'\4^1 a'\3^2

  % Three double stops expanding that harmony
  <a d'>4 \upbow
  <d' f'> \downbow
  <f' a'> \upbow
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \oneChordTexture
}


bowNuanceEtude = \absolute c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Triplet bow nuance study
  \tuplet 3/2 {
    % Tenuto – full value with weight
    \downbow a16-\tenuto \upbow b-\tenuto \downbow c'-\tenuto

    % Staccato – crisp separation
    \upbow d'-.
    \downbow e'-.
    \upbow f'-.

    % Accent – added emphasis
    \downbow g-\accent
    \upbow a-\accent
    \downbow b-\accent

    % Spiccato – suggested bounce (can be interpreted at tempo)
    \upbow c'-.
    \downbow d'-.
    \upbow e'-.
  }
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \bowNuanceEtude
}

doubleStopStudy = \relative c'' {
  \clef treble
  \key d \minor
  \time 4/4

  \once \override Fingering.direction = #UP
  \once \override StringNumber.direction = #DOWN

  % Broken double stop – played sequentially
  \downbow
  d8\3^1 f\2^2
  e\3^1 g\2^2
  f\3^1 a\2^3
  g\3^1 b\2^4

  % Double stops – played as two-note chords
  <d f>4^\markup { "I+II" } \upbow
  <e g> \downbow
  <f a> \upbow
  <g b> \downbow
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \doubleStopStudy
}

bowingExercise = \absolute c'' {
  \clef treble
  \key d \minor
  \time 4/4

  % Alternating between A and E strings, all downbow/upbow
  \once \override Fingering.direction = #UP
  \once \override StringNumber.direction = #DOWN

  \downbow a4\2^1
  \upbow e'\1^1
  \downbow a\2^1
  \upbow e'\1^1

  \downbow a\2
  \upbow e'\1
  \downbow a\2
  \upbow e'\1
}
\score {
  \new Staff \with {
    instrumentName = "Violin"
  } \bowingExercise
}