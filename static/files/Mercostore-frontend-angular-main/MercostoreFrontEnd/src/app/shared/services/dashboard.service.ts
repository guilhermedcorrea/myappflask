import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class DashBoardService {

  apiURL = 'http://localhost:3003/api/v1';
  constructor(private http:HttpClient) { }

  public getDashBoard(): Observable<any> {
    let token = localStorage.getItem('token');
     return this.http.get(`${this.apiURL}/dashboardCard?`,
      {headers: {
       "Authorization": `Bearer ${token}`
     }} );
   }
}
