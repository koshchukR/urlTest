import React, {useState} from 'react';
import css from './LoginScreen.module.css'
import {urlService} from "../services";
import {useNavigate} from "react-router-dom";

const LoginScreen = () => {
    const [data, setData] = useState({email: '', password: ''})
    const [error, setError] = useState(null)

    const navigate = useNavigate();


    const onButtonClick = () => {
        urlService.auth(data.email, data.password).then(data => {
            localStorage.setItem('token', data.data.access)
        })
            .then(data => navigate('/')).catch(e => setError('Something went wrong'))
    }
    return (
        <div className={css.container}>
            <span className={css.loginText}>Login</span>
            <input type="text" value={data.email} placeholder={'Enter email'}
                   onChange={(e) => setData({...data, email: e.target.value})}/>
            <input type="text" value={data.password} placeholder={'Enter password'}
                   onChange={(e) => setData({...data, password: e.target.value})}/>
            {error && <span className={css.text}>{error}</span>}
            <div className={css.buttons}>
                <button className={css.submit} onClick={onButtonClick}>Submit</button>
                <button className={css.register} onClick={() => navigate('/register')}>Register</button>
            </div>

        </div>
    );
};

export default LoginScreen;