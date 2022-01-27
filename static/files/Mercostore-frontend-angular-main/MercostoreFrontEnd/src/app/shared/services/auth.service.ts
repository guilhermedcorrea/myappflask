import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../models/user.model';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  apiURL = 'http://localhost:3003/api/v1';
  constructor(private http:HttpClient) { }

  public login(usuario: Usuario): Observable<any> {
    return this.http.post(`${this.apiURL}/login`, usuario);
  }
}

