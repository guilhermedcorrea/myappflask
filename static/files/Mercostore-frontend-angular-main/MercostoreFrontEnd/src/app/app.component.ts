import { ChangeDetectorRef, Component, AfterContentChecked } from '@angular/core';
import { LoadingService } from './shared/services/loading.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements AfterContentChecked {
  title = 'Mercostore';

  constructor(public loadingService: LoadingService, private cd:ChangeDetectorRef){

  }

  ngAfterContentChecked():void{
    this.cd.detectChanges()
  }
}
