import { Component, OnInit } from '@angular/core';
import { Time } from '../../api/times';
import { ConfirmationService, MessageService, SelectItem } from 'primeng/api';
import { TimeService } from 'src/app/service/time.service';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
    templateUrl: './time.component.html',
    providers: [MessageService, ConfirmationService],
    styleUrls: ['../../../assets/demo/badges.scss'],
})
export class TimeComponent implements OnInit {

    itemDialog: boolean;

    deleteItemDialog: boolean;

    items: Time[];

    item: Time;

    selectedItems: Time[];

    deleteItemsDialog: boolean = false;

    submitted: boolean;

    cols: any[];

    constructor(
        private service: TimeService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {

        this.service.getAll().subscribe((x) => {
            this.items = this.sortByDescending(x.Time);
            console.log(this.items);
        });

        this.cols = [
            { field: 'Id', header: 'Id' },
            { field: 'Name', header: 'Name' },
            { field: 'Day', header: 'Day' },
            { field: 'TimeGroups', header: 'TimeGroups' },
        ];

    }

    deleteSelectedItems() {
        this.deleteItemsDialog = true;
    }

    openNew(): void {
        this.item = null;
        this.submitted = false;
        this.itemDialog = true;
    }

    editItem(item: Time): void {
        this.item = { ...item };
        this.itemDialog = true;
    }

    hideDialog(): void {
        this.itemDialog = false;
        this.submitted = false;
        this.item = null;
    }

    hideDeleteItemsDialog(): void {
        this.deleteItemsDialog = false;
        this.submitted = false;
    }

    confirmDeleteSelected() {
        // this.submitted = true;
        // this.selectedItems.forEach(x => {
        //     this.service.delete(x.id).subscribe(
        //         {
        //             next: () => {
        //                 this.messageService.add({
        //                     severity: 'success',
        //                     summary: 'Sucesso',
        //                     detail: 'Item deletado',
        //                     life: 3000
        //                 });

        //                 this.items = this.items.filter(item => item.id !== x.id);
        //             },
        //             error: (err: HttpErrorResponse) => {
        //                 this.messageService.add({
        //                     severity: 'error',
        //                     summary: 'Erro',
        //                     detail: err.error?.message,
        //                     life: 3000
        //                 });
        //                 console.error(err);
        //             },
        //             complete: () => {
        //                 this.hideDeleteItemsDialog();
        //             }
        //         }
        //     );
        // });
    }

    saveItem(): void {
        // this.submitted = true;
        // if (this.item.name.trim()) {
        //     if (this.item.id) {
        //         this.service.update(this.item)
        //             .subscribe(
        //                 {
        //                     next: (x) => {
        //                         this.items[this.findIndexById(this.item.id)] = x;
        //                         this.messageService.add({
        //                             severity: 'success',
        //                             summary: 'Sucesso',
        //                             detail: 'Dados atualizados',
        //                             life: 3000
        //                         });
        //                     },
        //                     error: (err: HttpErrorResponse) => {
        //                         this.messageService.add({
        //                             severity: 'error',
        //                             summary: 'Erro',
        //                             detail: err.error?.message,
        //                             life: 3000
        //                         });
        //                         console.error(err);
        //                     },
        //                     complete: () => {
        //                         this.saveItemComplete();
        //                     }
        //                 }
        //             );
        //     } else {
        //         this.service.create(this.item)
        //             .subscribe(
        //                 {
        //                     next: (x: Time) => {
        //                         this.items.unshift(x);
        //                         this.messageService.add({
        //                             severity: 'success',
        //                             summary: 'Sucesso',
        //                             detail: 'Item criado com sucesso.',
        //                             life: 3000
        //                         });
        //                     },
        //                     error: (err: HttpErrorResponse) => {
        //                         this.messageService.add({
        //                             severity: 'error',
        //                             summary: 'Erro',
        //                             detail: 'Erro ao realizar cadastro. ' + err?.error?.message,
        //                             life: 3000
        //                         });
        //                         console.error(err);
        //                     },
        //                     complete: () => {
        //                         this.saveItemComplete();
        //                     }
        //                 }
        //             );
        //     }

        // }
    }

    // findIndexById(id: string): number {
    //     let index = -1;
    //     for (let i = 0; i < this.items.length; i++) {
    //         if (this.items[i].id === id) {
    //             index = i;
    //             break;
    //         }
    //     }

    //     return index;
    // }

    saveItemComplete(): void {
        this.items = [...this.items];
        this.hideDialog();
    }

    sortByDescending(x: Time[]): Time[] {
        return x.sort((a, b) => b.Id.localeCompare(a.Id));
    }
}
