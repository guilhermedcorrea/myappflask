import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import { AuthService } from '../../../shared/services/auth.service';
import { Usuario } from 'src/app/shared/models/user.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public formularioLogin: FormGroup = new FormGroup({
    email: new FormControl(null, [Validators.required, Validators.email]),
    senha: new FormControl(null, [Validators.required])
  });
  
  hide = true;
  erromsg = false;

  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }

  public auth():void{
    const usuario: Usuario = new Usuario(
      this.formularioLogin.value.email,
      this.formularioLogin.value.senha
    );

    this.authService.login(usuario)
      .subscribe(res => {
        console.log(res.content)
        localStorage.setItem('token', res.content.token);
        if (res.content.user.Privilegio === 'Administrador') {
          localStorage.setItem('ADM', 'true')
        } else {
          localStorage.setItem('ADM', 'false')
        }
        this.route.navigate(['home'])
      },
      erro => {
        this.erromsg = true
      })
  }

  public hidemsg():void{
    this.erromsg = false;
  }
}
