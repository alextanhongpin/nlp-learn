## Text segmentation

How do we segment this text `thequickbrownfoxjumpsoverthelazydog` into `the quick brown fox jumps over the lazy dog`? A naive approach will be:
```js
// const word = 'thisisamazing'
// const word = 'thereissomeamazingtruth'
const word = 'thequickbrownfoxjumpsoverthelazydog'

const dictionary = {
  'this': true,
  'is': true,
  'amazing': true,
  'there': true,
  'some': true,
  'truth': true,
  // 'the': true // This will spoil the result.
}

// This method does not work. How to decide whether to choose between "the" and "there"? We still need to compute the best prefix probability matches.
function segmentWord(word, n = 0) {
  if (n > word.length) return []
  const left = word.slice(0, n)
  const right = word.slice(n)
  if (dictionary[left]) {
    return [left].concat(segmentWord(right, 0))
  }
  return segmentWord(word, n + 1)
}

console.log(segmentWord(word))
```

Alternative way:
```js
// The probabilities should be taken from a corpus of words/dictionary and the number of times they appear.
const probabilities = {
  it: 0.2,
  is: 0.4,
  i: 0.6,
  sit: 0.4,
  there: 0.2,
  some: 0.1,
  amazing: 0.5,
  truth: 0.4,
  the: 1,
  quick: 1,
  brown: 1,
  fox: 1,
  jumps: 1,
  over: 1,
  lazy: 1,
  dog: 1
}

function getProbability(word) {
  return probabilities[word] || 0
}

function triangularMatrixAlgorithm(word, n = 0) {
  let table = {}
  for (let i = 1; i < word.length; i++) {
    const left = word.substring(0, i)
    const probLeft = getProbability(left)
    if (probLeft) {
      table[[left, 0, i]] = {
        word: left,
        prob: probLeft,
        start: 0,
        end: i
      }
    }
    for (let j = i; j < word.length + 1; j++) {
      const right = word.substring(i, j)
      const probRight = getProbability(right)
      console.log(left, right)

      if (probRight) {
        table[[right, i, j]] = {
          word: right,
          prob: probRight,
          start: i,
          end: j
        }
        break
      }
    }
  }
  return table
}

const result = triangularMatrixAlgorithm(word)
console.log('result', result)
const output = Object.values(result)

const graph = {}
for (let item of output) {
  graph[item.start] = item
}
console.log(output, graph)

let next = 0
while (graph[next]) {
  const item = graph[next]
  console.log(item.word)
  next = item.end
}
```
