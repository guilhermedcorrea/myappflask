import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(protected router: Router) { }

  verificarAcesso(state: string): Observable<boolean> | boolean {
    if ((!localStorage.getItem('token'))) {
      this.router.navigate(['acesso']);
      return false;
    }
    return true;
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot ): Observable<boolean> | boolean {
    return this.verificarAcesso(state.url);
  }
}