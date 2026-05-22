# React Material UI to Angular Material Component Mapping

| React JSX Tag (MUI or Standard) | Angular Material Selector | Required Angular Import Module |
| :--- | :--- | :--- |
| `<Button variant="contained">` | `<button mat-raised-button>` | `MatButtonModule` |
| `<Button variant="outlined">` | `<button mat-stroked-button>` | `MatButtonModule` |
| `<TextField label="Email">` | `<mat-form-field><mat-label>Email</mat-label><input matInput></mat-form-field>` | `MatInputModule, MatFormFieldModule` |
| `<Select label="Age">` | `<mat-form-field><mat-label>Age</mat-label><mat-select><mat-option value="1">1</mat-option></mat-select></mat-form-field>` | `MatSelectModule, MatFormFieldModule` |
| `<Card>` | `<mat-card>` | `MatCardModule` |
| `<CardContent>` | `<mat-card-content>` | `MatCardModule` |
| `<Dialog>` | Uses `MatDialog` Service | `MatDialogModule` |
