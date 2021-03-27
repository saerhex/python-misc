import React, {useState} from 'react'
import InputBox from "../Input/InputBox";

const Translation = () => {
  const [word, setWord] = useState("")
  const [translated, setTranslated] = useState("")

  const fetchTranslate = async (e) => {
    e.preventDefault()
    const resp = await fetch("/translate/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        },
        body: JSON.stringify({wordReq: word})
      }
    )

    if (resp.status === 404) {
      alert("Failed!")
    } else {
      const data = await resp.json()
      setTranslated(data["translated"])
      console.log("Successfully sent words!")
    }
  }

  return (
    <InputBox word={word}
              setWord={setWord}
              translated={translated}
              setTranslated={setTranslated}
              clickHandler={fetchTranslate}
              term={!!word}
              btnValue={"Translate"}/>
  )
}

export default Translation