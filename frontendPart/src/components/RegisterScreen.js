import React, {useState} from 'react';
import css from './RegisterScreen.module.css'
import {urlService} from "../services";
import {useNavigate} from "react-router-dom";

const RegisterScreen = () => {
    const [data, setData] = useState({email: '', password: '', name: '', surname: ''})
    const [isRegistered, setIsRegistered] = useState(false)
    const [error, setError] = useState(null)

    const navigate = useNavigate();


    const onButtonClick = () => {
        urlService.register(data.email, data.password, data.name, data.surname).then(data => {setIsRegistered(true);setError(null); setData({email: '', password: '', name: '', surname: ''})})
            .catch(e => setError('Something went wrong'))
    }
    return (
        <div className={css.container}>
            <span className={css.registerText}>Register</span>
            <input type="text" placeholder={'Enter email'} value={data.email}
                   onChange={(e) => setData({...data, email: e.target.value})}/>
            <input type="text" placeholder={'Enter password'} value={data.password}
                   onChange={(e) => setData({...data, password: e.target.value})}/>
            <input type="text" placeholder={'Enter name'} value={data.name}
                   onChange={(e) => setData({...data, name: e.target.value})}/>
            <input type="text" placeholder={'Enter surname'} value={data.surname}
                   onChange={(e) => setData({...data, surname: e.target.value})}/>
            {error && <span className={css.text}>{error}</span>}
            {isRegistered && <span className={css.textSuccessfully}>Successfully registered</span>}
            <div className={css.buttons}>
                <button className={css.submit} onClick={onButtonClick}>Submit</button>
                <button className={css.back} onClick={() => navigate('/login')}>{'<- Back'}</button>
            </div>

        </div>
    );
};

export default RegisterScreen;