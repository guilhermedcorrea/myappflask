import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { MenuComponent } from './shared/components/menu/menu.component';
import { AuthGuard } from './shared/guards/auth-guard';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'acesso' },
  {
    path: 'acesso',
    loadChildren: () => import('./modules/acesso/acesso.module').then(m => m.AcessoModule)
  },
  {
    path: 'home',
    component: MenuComponent,
    canActivate: [ AuthGuard ],
    children: [
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'dashboard'
      },
      { 
        path: 'produtos',
        loadChildren: () => import('./modules/produtos/produtos.module').then(m => m.ProdutosModule)
      },
      { 
        path: 'dashboard',
        loadChildren: () => import('./modules/painel/painel.module').then(m => m.PainelModule)
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
