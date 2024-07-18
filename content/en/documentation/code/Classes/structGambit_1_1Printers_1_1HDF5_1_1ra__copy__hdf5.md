---
title: "struct Gambit::Printers::HDF5::ra_copy_hdf5"

description: "[No description available]"

---

# struct Gambit::Printers::HDF5::ra_copy_hdf5



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename U \> <br>void | **[run](/documentation/code/classes/structgambit_1_1printers_1_1hdf5_1_1ra__copy__hdf5/#function-run)**(U , hid_t & dataset_out, hid_t & dataset2_out, std::vector< hid_t > & datasets, std::vector< hid_t > & datasets2, const unsigned long long size, const std::unordered_map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), unsigned long long, [PPIDHash](/documentation/code/classes/structgambit_1_1printers_1_1ppidhash/), [PPIDEqual](/documentation/code/classes/structgambit_1_1printers_1_1ppidequal/) > & RA_write_hash, const std::vector< std::vector< unsigned long long > > & pointid, const std::vector< std::vector< unsigned long long > > & rank, const std::vector< unsigned long long > & aux_sizes, hid_t & , hid_t & ) |

## Public Functions Documentation

### function run

```
template <typename U >
static inline void run(
    U ,
    hid_t & dataset_out,
    hid_t & dataset2_out,
    std::vector< hid_t > & datasets,
    std::vector< hid_t > & datasets2,
    const unsigned long long size,
    const std::unordered_map< PPIDpair, unsigned long long, PPIDHash, PPIDEqual > & RA_write_hash,
    const std::vector< std::vector< unsigned long long > > & pointid,
    const std::vector< std::vector< unsigned long long > > & rank,
    const std::vector< unsigned long long > & aux_sizes,
    hid_t & ,
    hid_t & 
)
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000