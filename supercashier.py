item = {} #Dict untuk menampung nama, jumlah, dan harga barang 

class Transaction():
    
    def __init__(self):
        '''
        Pass agar tidak perlu memasukkan
        atribut di kelas Transaction
        '''
        pass
    
    def add_item(self, barang, qty, harga):
        '''
        Fungsi untuk input nama barang, jumlah barang
        dan harga barang
        
        PARAMETER:
        barang: Nama barang yang dibeli (str)
        qty: Qunatity atau jumlah barang yang dibeli (int)
        harga: Harga barang yang dibeli (int)
        '''
        try:
            barang = barang.title()
            qty = int(qty)
            harga = int(harga)
            item[barang] = [qty, harga] #Menambahkan pada Dict item
        except TypeError:
            pass
    
    def update_item_name(self, barang, update_barang):
        '''
        Fungsi untuk mengubah atau memperbaiki
        nama barang yang dibeli
        
        PARAMETER:
        barang: Nama barang yang ingin diubah
        update_barang: Nama barang yang diinginkan
        '''
        try:
            barang = barang.title()
            update_barang = update_barang.title()
            item[update_barang] = item[barang]
            item.pop(barang)
        except:
            pass
    
    def update_item_qty(self, barang, update_qty):
        '''
        Fungsi untuk mengubah atau memperbaiki
        jumlah barang yang dibeli
        
        PARAMETER:
        barang: Nama barang yang ingin jumlahnya diubah
        update_qty: Jumlah barang yang diinginkan
        '''
        try:
            barang = barang.title()
            item[barang][0] = update_qty
        except:
            pass
    
    def update_item_price(self, barang, update_price):
        '''
        Fungsi untuk mengubah atau memperbaiki
        harga barang yang dibeli
        
        PARAMETER:
        barang: Nama barang yang ingin jumlahnya diubah
        update_price: Harga barang yang diinginkan
        '''
        try:
            barang = barang.title()
            item[barang][1] = update_price
        except:
            pass
        
    def delete_item(self, barang):
        '''
        Fungsi untuk menghapus barang yang tidak
        diinginkan
        '''
        try:
            barang = barang.title()
            item.pop(barang)
        except:
            pass
    
    def reset_transaction(self):
        '''
        Fungsi untuk menghapus semua barang
        yang dipesan
        '''
        try:
            item.clear()
            print('Semua item berhasil di delete!')
        except:
            pass
    
    def check_order(self):
        '''
        Fungsi untuk memeriksa benar atau salahnya pesanan yang 
        sudah diinput dan menampilkan seluruh barang yang
        dipesan
        '''
        try:
            for key, values in item.items():
                barang = key
                qty = values[0]
                harga = values[1]
                barang = barang.title()
            
                if type(barang) != str:
                    print('Salah input barang')
                elif type(qty) != int:
                    print('Salah input jumlah')
                elif type(harga) != int:
                    print('Salah input harga')
                else:
                    print("Pemesanan sudah benar!")
            print(f'Belanjaan anda {item}')
        except:
            pass
    
    def total_price(self):
        '''
        Fungsi untuk mengetahui total dari belanja yang harus
        dibayar beserta diskon yang didapatkan
        '''
        try:
            item_barang = []
            total_harga = 0
            for key, values in item.items():
                barang = key
                qty = values[0]
                harga = values[1]
                barang = barang.title()
                item_barang.append(barang)
                total_harga_barang = qty*harga
                total_harga += total_harga_barang
        
            #Mencari diskon
            if total_harga > 500000:
                diskon = 0.1
                total_diskon = total_harga*diskon
                total_harga_diskon = total_harga-total_diskon
                pesan = f"total belanja Rp{total_harga}. Selamat! Anda mendapatkan diskon {int(diskon*100)}%. Anda menghemat Rp{int(total_diskon)} dan hanya perlu membayar Rp{int(total_harga_diskon)}."            
            elif total_harga > 300000:
                diskon = 0.08
                total_diskon = total_harga*diskon
                total_harga_diskon = total_harga-total_diskon
                pesan = f"total belanja Rp{total_harga}. Selamat! Anda mendapatkan diskon {int(diskon*100)}%. Anda menghemat Rp{int(total_diskon)} dan hanya perlu membayar Rp{int(total_harga_diskon)}."
            elif total_harga > 200000:
                diskon = 0.05
                total_diskon = total_harga*diskon
                total_harga_diskon = total_harga-total_diskon
                pesan = f"total belanja Rp{total_harga}. Selamat! Anda mendapatkan diskon {int(diskon*100)}%. Anda menghemat Rp{int(total_diskon)} dan hanya perlu membayar Rp{int(total_harga_diskon)}."
            else:
                pesan = (f'total belanja Rp{total_harga}. Anda perlu belanja minimal Rp200000 agar mendapatkan diskon.')
            print(f'Anda membeli {item_barang} dengan {pesan}')
        except:
            pass
                
        
                
            
            
            