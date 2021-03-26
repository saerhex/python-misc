import React from "react"
import 'materialize-css'

const InputBox = ({word, setWord, translated, setTranslated, clickHandler, term, btnValue}) => {
  return (
    <div className="container">
      <form onSubmit={clickHandler} className="col s6">
        <div className="row center s6 center">
          <div className="input-field col s6">
            <input id="rus"
                   type="text"
                   value={word}
                   onChange={e => setWord(e.target.value)}
            />
            <label htmlFor="rus">Words on russian</label>
          </div>
          <div className="input-field col s6">
            <input id="en"
                   type="text"
                   value={translated}
                   onChange={e => setTranslated(e.target.value)}
            />
            <label htmlFor="en" className="right">Words on english</label>
          </div>
        </div>
        <div className="col center">
          <input className="waves-effect waves-light btn"
                 type="submit"
                 value={btnValue}
                 disabled={!term}
          />
        </div>
      </form>
    </div>)
}

export default InputBox