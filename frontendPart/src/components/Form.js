import React, {useState} from 'react';

import css from './Form.module.css'
import {urlService} from "../services";
import {useNavigate} from "react-router-dom";

const Form = () => {

    const [value, setValue] = useState(null)
    const [error, setError] = useState(null)
    const [data, setData] = useState(null)
    const [isLoading, setIsLoading] = useState(false)
    const navigate = useNavigate();

    const handleInputError = (value) => {
        if (value.status === 401) {
            setError('You must be logged in!')
        } else setError(value?.data?.message ? value.data.message : 'This field can not be blank.')
        setData('')
        setIsLoading(false)
    }

    const handleInputData = (data) => {
        setData(data)
        setError('')
        // setValue('')
        setIsLoading(false)
    }

    const submit = (url) => {
        const token = localStorage.getItem('token');
        setError('')
        setData('')
        setIsLoading(true)
        urlService.checkUrl(url, token).then(data => handleInputData(data.data)).catch(e => {
            handleInputError(e.response)
        })
    }

    const onLoginClick = () => {
        navigate('/login')
    }
    return (
        <div className={css.formDiv}>
            <div className={css.inputButtonDiv}>
                <input type="text" onChange={(e) => setValue(e.target.value)} value={value} placeholder={'Enter url'}/>
                <button className={css.check} onClick={() => value ? submit(value) : handleInputError("This field can not be blank.")}>Check
                </button>
                <button className={css.login} onClick={onLoginClick}>Login</button>
            </div>
            {isLoading && <span className={css.loader}></span>}
            {error && <div className={css.errorText}>{error}</div>}
            {data &&
                <div className={css.data}>
                    <div className={css.text}>• {data['domain_result']['message']} <span className={css.score}>Risk score - {data['domain_result']['risk_score']}</span>
                    </div>
                    <div className={css.text}>• {data['content_result']['message']} <span className={css.score}>Risk score - {data['content_result']['risk_score']}</span>
                    </div>
                    <div className={css.text}>• {data['transmit_data_result']['message']} <span className={css.score}>Risk score
                        - {data['transmit_data_result']['risk_score']}</span></div>
                    <div className={css.result}>Overall Risk - {data['overall_risk']}</div>
                </div>
            }

        </div>
    );
};

export default Form;