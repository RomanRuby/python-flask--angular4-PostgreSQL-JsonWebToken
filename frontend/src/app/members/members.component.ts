import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import {HttpClient} from "@angular/common/http";
import { GlobalVariable } from '../auth.service';
import "rxjs/add/operator/map";
import {Observable} from "rxjs/Observable";
import {any} from "codelyzer/util/function";

@Component({
    selector: 'app-members',
    templateUrl: './members.component.html',
    styleUrls: ['./members.component.css']
})
export class MembersComponent implements OnInit {
    cars : any;
    holders : any;
    accountData: any;
    constructor(private authService: AuthService,private http: HttpClient, private router: Router) { }

    ngOnInit() {
        this.authService.getAccount().subscribe(
            (res: any) => {
                this.accountData = res;
            }, (err: any) => {
                this.router.navigateByUrl('/login');
            }
        );

        this.authService.getHolders().subscribe(
            (res: any) => {
                this.holders = res;
                console.log(this.holders)
            }, (err: any) => {
                this.router.navigateByUrl('/login');
            }
        );

        this.authService.getCars().subscribe(
            (res: any) => {
                this.cars = res;
                console.log(this.cars)
            }, (err: any) => {
                this.router.navigateByUrl('/login');
            }
        );

    }



}
