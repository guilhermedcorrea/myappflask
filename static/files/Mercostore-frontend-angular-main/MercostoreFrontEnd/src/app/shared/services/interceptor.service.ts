import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';
import { LoadingService } from './loading.service';

@Injectable({
  providedIn: 'root'
})
export class InterceptorService implements HttpInterceptor {

  constructor(public loadingService: LoadingService) { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    this.loadingService.isLoading.next(true);

    return next.handle(req).pipe(
      finalize(
        () => {
          this.loadingService.isLoading.next(false);
        }
      )
    );
  }
}