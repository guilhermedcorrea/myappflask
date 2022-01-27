import { Component, OnInit } from '@angular/core';
import { DashBoardService } from 'src/app/shared/services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  public dashBoardCard: Array<{titulo: string, porcentagem: number}> = [];
  constructor(private dashboardService: DashBoardService) { }

  ngOnInit(): void {
    this.loadDashBoard()
  }

  public loadDashBoard():void{
    this.dashboardService.getDashBoard()
      .subscribe(res => {
        console.log(res)
        this.dashBoardCard.push({
          titulo: 'Abaixo Preço',
          porcentagem: res.dashboard[0].AbaixoPreco
        });
        this.dashBoardCard.push({
          titulo: 'Acima Preço',
          porcentagem: res.dashboard[0].AcimaPreco
        });
        this.dashBoardCard.push({
          titulo: 'Dentro Preço',
          porcentagem: res.dashboard[0].DentroPreco
        });
        this.dashBoardCard.push({
          titulo: 'Não Tem Preço',
          porcentagem: res.dashboard[0].NaoTemPreco
        })
        console.log(this.dashBoardCard)
      })
  }

}
