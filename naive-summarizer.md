## Text summarization

Can we create a simple text summarization just purely based on the frequency of the words.

```js
const STOPWORDS = new Set(['a', 'and', 'the', 'to', 'in', 'as', 'of', 'be', 'for', 'were', 'can', 'that', 'is', 'or'])

const text = `A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs. These programs enable computers to perform an extremely wide range of tasks. A "complete" computer including the hardware, the operating system (main software), and peripheral equipment required and used for "full" operation can be referred to as a computer system. This term may as well be used for a group of computers that are connected and work together, in particular a computer network or computer cluster.

Computers are used as control systems for a wide variety of industrial and consumer devices. This includes simple special purpose devices like microwave ovens and remote controls, factory devices such as industrial robots and computer-aided design, and also general purpose devices like personal computers and mobile devices such as smartphones. The Internet is run on computers and it connects hundreds of millions of other computers and their users.

Early computers were only conceived as calculating devices. Since ancient times, simple manual devices like the abacus aided people in doing calculations. Early in the Industrial Revolution, some mechanical devices were built to automate long tedious tasks, such as guiding patterns for looms. More sophisticated electrical machines did specialized analog calculations in the early 20th century. The first digital electronic calculating machines were developed during World War II. The first semiconductor transistors in the late 1940s were followed by the silicon-based MOSFET (MOS transistor) and monolithic integrated circuit (IC) chip technologies in the late 1950s, leading to the microprocessor and the microcomputer revolution in the 1970s. The speed, power and versatility of computers have been increasing dramatically ever since then, with MOS transistor counts increasing at a rapid pace (as predicted by Moore's law), leading to the Digital Revolution during the late 20th to early 21st centuries.

Conventionally, a modern computer consists of at least one processing element, typically a central processing unit (CPU) in the form of a metal-oxide-semiconductor (MOS) microprocessor, along with some type of computer memory, typically MOS semiconductor memory chips. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored information. Peripheral devices include input devices (keyboards, mice, joystick, etc.), output devices (monitor screens, printers, etc.), and input/output devices that perform both functions (e.g., the 2000s-era touchscreen). Peripheral devices allow information to be retrieved from an external source and they enable the result of operations to be saved and retrieved.`

console.log(summarize(text))

function summarize(text, paragraph = 3) {
  const bow = bagOfWords(text)
  const top20 = topN(bow, 30)
  const scores = tokenizeSentence(text).map((sentence, i) => {
    return {
      i,
      sentence,
      // Alternatively, count the words only once using Set.
      score: tokenizeWord(sentence).reduce((score, word) => {
        return score + (top20[word] || 0)
      }, 0)
    }
  })
  const summarized = scores.sort((l, r) => {
      return r.score - l.score
    })
    .slice(0, paragraph)
    .sort((l, r) => {
      return l.i - r.i
    }).map(item => item.sentence.trim())
  // To ensure that the last sentence has a full-stop.
  summarized.push('')
  return summarized.join('. ').trim()
}

function removeNewline(text) {
  // ?:  is for non capturing group
  return text.replace(/(?:\r\n|\r|\n)/gm, '')
}

function tokenizeWord(sentence) {
  return sentence.trim()
    .split(' ')
    .map(word => word.replace(/\W/g, ''))
    .map(word => word.trim())
    .filter(Boolean)
    .filter(stopwords)
}

function tokenizeSentence(text) {
  return removeNewline(text)
    .split('.')
}

function stopwords(word) {
  return !STOPWORDS.has(word)
}

function tokenizeCorpus(text) {
  text = text.trim().toLowerCase()
  return tokenizeSentence(text)
    .flatMap(tokenizeWord)
}

function bagOfWords(text) {
  const tokens = tokenizeCorpus(text)
  return tokens.reduce((counter, word) => {
    counter[word] = counter[word] ? counter[word] + 1 : 1
    return counter
  }, {})
}

function topN(counter, n = 20) {
  const sorted = Object.entries(counter).sort((l, r) => {
    const [_lkey, lscore] = l
    const [_rkey, rscore] = r
    return rscore - lscore
  })
  return sorted.slice(0, n).reduce((acc, [word, score]) => {
    acc[word] = score
    return acc
  }, {})
}
```
