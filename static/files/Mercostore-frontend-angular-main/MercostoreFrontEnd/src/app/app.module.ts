import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AuthService } from './shared/services/auth.service';
import { SharedModule } from './shared/shared.module';
import { InterceptorService } from './shared/services/interceptor.service';
import { LOCALE_ID } from '@angular/core';
import { registerLocaleData } from '@angular/common';
import ptBr from '@angular/common/locales/pt';
registerLocaleData(ptBr);
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    SharedModule
  ],
  providers: [
    AuthService,
    {provide:HTTP_INTERCEPTORS, useClass:InterceptorService, multi:true},
    { provide: LOCALE_ID, useValue: 'pt-PT' }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
