import React from 'react'
import 'materialize-css'

const InputBox = ({word, setWord, translated, setTranslated, clickHandler, term, btnValue}) => (
  <div className="container">
    <form onSubmit={clickHandler} className="col s6 lxnd-bold">
      <div className="row center s6 center">
        <div className="input-field col s6">
          <input className="lxnd-bold"
                 id="rus"
                 type="text"
                 value={word}
                 onChange={e => setWord(e.target.value)}
          />
          <label htmlFor="rus">Words on russian</label>
        </div>
        {btnValue !== 'Translate' ? <div className="input-field">
          <input className="lxnd-bold"
                 id="en"
                 type="text"
                 value={translated}
                 onChange={e => setTranslated(e.target.value)}
          />
          <label htmlFor="en">Words on english</label>
        </div> : <div className="section"><span className="left">Translation: {translated}</span></div>
        }
      </div>
      <div className="col center">
        <input className="waves-effect waves-light btn"
               type="submit"
               value={btnValue}
               disabled={!term}
        />
      </div>
    </form>
  </div>
)

export default InputBox