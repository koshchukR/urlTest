import {axiosService} from "./axiosService";
import {urls} from "../configs";

const urlService = {
    checkUrl: (url, token) => axiosService.post(urls.check_url, {'url': url}, {headers: {
    'Authorization': `Bearer ${token}`
  }}),
    auth: (email, password) => axiosService.post(urls.auth, {email, password}),
    register: (email, password, name, surname) => axiosService.post(urls.register , {email, password, profile: {name, surname}}),
}

export {
    urlService
}