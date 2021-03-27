import React, {useState} from 'react'
import InputBox from "./InputBox";

const WordsInput = () => {
  const [word, setWord] = useState(null)
  const [translated, setTranslated] = useState(null)

  const sendWords = async (e) => {
    e.preventDefault()
    const resp = await fetch("/add-words/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8'
      },
      body: JSON.stringify({wordReq: word, translateReq: translated})
    })
    if (resp.status === 404) {
      alert("Failed!")
    } else {
      console.log("Successfully sent words!")
    }
  }

  return (
    <InputBox word={word}
              setWord={setWord}
              translated={translated}
              setTranslated={setTranslated}
              clickHandler={sendWords}
              term={!!word && !!translated}
              btnValue={"Add translation"}
    />
  )

}

export default WordsInput;
