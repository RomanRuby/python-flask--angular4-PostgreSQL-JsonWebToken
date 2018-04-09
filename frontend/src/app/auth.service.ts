import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';

 export const GlobalVariable = Object.freeze({
      API_URL : 'http://localhost:5000'
 });

@Injectable()
export class AuthService {

    TOKEN_KEY = 'access_token';


    constructor(private http: HttpClient, private router: Router) { }

    get token() {
        return localStorage.getItem(this.TOKEN_KEY);
    }

    get isAuthenticated() {
        return !!localStorage.getItem(this.TOKEN_KEY);
    }


    logout() {
        localStorage.removeItem(this.TOKEN_KEY);
        this.router.navigateByUrl('/');
    }

    login(login: string, pass: string) {
        const headers = {
            headers: new HttpHeaders(
              { 'Content-Type': 'application/json', 'Cache-Control': 'no-cache' })
        };



        const data = {
            username: login,
            password: pass
        };
        console.log(data);

        this.http.post(GlobalVariable.API_URL + '/auth', data, headers).subscribe(
            (res: any) => {
                console.log(this.TOKEN_KEY, res['access_token']);
                localStorage.setItem(this.TOKEN_KEY, res['access_token']);
                console.log(localStorage);

                this.router.navigateByUrl('/members');
            }
        );
    }

    getAccount() {
        return this.http.get(GlobalVariable.API_URL + '/account');
    }

    getCars() {
      return this.http.get(GlobalVariable.API_URL + '/cars');
    }

    getHolders() {
        return this.http.get(GlobalVariable.API_URL + '/holders')
    }
}
